import os
import cv2
import csv
import rclpy
from rclpy.serialization import deserialize_message
from rosidl_runtime_py.utilities import get_message
import rosbag2_py
from cv_bridge import CvBridge

def export_bag_data(bag_file_path, output_dir):
    # Klasörleri oluştur
    img_dir = os.path.join(output_dir, "images")
    os.makedirs(img_dir, exist_ok=True)
    
    # CSV dosyalarını hazırla
    csv_files = {
        "/lunarsim/imu": open(os.path.join(output_dir, "imu_data.csv"), "w", newline=""),
        "/lunarsim/gt/pose": open(os.path.join(output_dir, "pose_data.csv"), "w", newline=""),
        "/cmd_vel": open(os.path.join(output_dir, "velocity_data.csv"), "w", newline="")
    }
    
    writers = {}
    bridge = CvBridge()

    # Bag okuyucu ayarları
    reader = rosbag2_py.SequentialReader()
    storage_options = rosbag2_py.StorageOptions(uri=bag_file_path, storage_id="sqlite3")
    converter_options = rosbag2_py.ConverterOptions(
        input_serialization_format="cdr", output_serialization_format="cdr"
    )
    reader.open(storage_options, converter_options)

    topic_types = reader.get_all_topics_and_types()
    type_map = {topic.name: topic.type for topic in topic_types}

    print(f"Veriler ayıklanıyor: {bag_file_path}")

    while reader.has_next():
        (topic, data, t) = reader.read_next()
        msg_type = get_message(type_map[topic])
        msg = deserialize_message(data, msg_type)

        # 1. Görüntü Ayıklama (WebP)
        if topic == "/lunarsim/camera_left/raw":
            cv_img = bridge.imgmsg_to_cv2(msg, desired_encoding="passthrough")
            filename = f"frame_{t}.webp"
            cv2.imwrite(os.path.join(img_dir, filename), cv_img, [cv2.IMWRITE_WEBP_QUALITY, 90])
            
        # 2. Sayısal Veri Ayıklama (CSV)
        elif topic in csv_files:
            file = csv_files[topic]
            if topic not in writers:
                # Başlıkları ilk satıra yaz
                if topic == "/lunarsim/imu":
                    headers = ["timestamp", "accel_x", "accel_y", "accel_z", "gyro_x", "gyro_y", "gyro_z"]
                elif topic == "/lunarsim/gt/pose":
                    headers = ["timestamp", "pos_x", "pos_y", "pos_z", "ori_x", "ori_y", "ori_z", "ori_w"]
                elif topic == "/cmd_vel":
                    headers = ["timestamp", "linear_x", "angular_z"]
                
                writers[topic] = csv.writer(file)
                writers[topic].writerow(headers)

            # Verileri satır olarak ekle
            if topic == "/lunarsim/imu":
                writers[topic].writerow([t, msg.linear_acceleration.x, msg.linear_acceleration.y, msg.linear_acceleration.z,
                                         msg.angular_velocity.x, msg.angular_velocity.y, msg.angular_velocity.z])
            elif topic == "/lunarsim/gt/pose":
                writers[topic].writerow([t, msg.pose.position.x, msg.pose.position.y, msg.pose.position.z,
                                         msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w])
            elif topic == "/cmd_vel":
                writers[topic].writerow([t, msg.linear.x, msg.angular.z])

    # Dosyaları kapat
    for f in csv_files.values():
        f.close()
    
    print(f"İşlem Tamamlandı! Çıktılar burada: {output_dir}")

if __name__ == "__main__":
    # Örnek kullanım (Konteynır içindeki yollara göre)
    bag_path = "/root/lunarsim/data/tum_veriler/tum_veriler_0.db3"
    out_path = "/root/lunarsim/data/ayiklanmis_veriler"
    
    if os.path.exists(bag_path):
        export_bag_data(bag_path, out_path)
    else:
        print(f"Hata: {bag_path} dosyası bulunamadı!")
