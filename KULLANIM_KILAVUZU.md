# LunarSim Kullanım Kılavuzu

Bu kılavuz, simülatörü başlatma, robotu hareket ettirme ve verileri masaüstüne kaydetme adımlarını içerir.

## 1. Terminal: Simülatörü Başlatma
Bu terminalde simülatörün grafik arayüzü çalışır.

```bash
# Proje dizinine git
cd ~/Desktop/LunarSim

# Konteynırı başlat (GPU ve Paylaşımlı Klasör ile)
sg docker -c "./run.sh"

# Konteynır içinde simülatörü çalıştır
./LunarSim.x86_64
```
*(Bu terminali kapatmayın, simülatör burada açık kalmalı.)*

## 2. Terminal: Kontrol ve Veri Kaydı
Bu terminalde robotu yönetir ve verileri kaydedersiniz.

### Konteynıra Bağlanma ve ROS Aktif Etme
```bash
# Konteynıra gir
sg docker -c "docker exec -it lunarsim bash"

# ROS 2 ortamını aktif et (HER SEFERİNDE YAPILMALI)
source /opt/ros/humble/setup.bash
```

### Robotu Hareket Ettirme (Örnek Komut)
```bash
ros2 topic pub --once /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.5, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.1}}"
```

### Verileri Masaüstüne Kaydetme (ros2 bag)
Konteynır içindeki `/root/lunarsim/data` klasörü, masaüstündeki `LunarSim/data` klasörü ile senkronizedir.

```bash
# Veri klasörüne git
cd /root/lunarsim/data

# Kaydı başlat (Sol kamera ve hız verileri)
ros2 bag record -o rover_verileri /lunarsim/camera_left/raw /cmd_vel /lunarsim/imu
```
*   Kaydı durdurmak için: **Ctrl + C**
*   Kayıt bittiğinde masaüstündeki `LunarSim/data/rover_verileri` klasörüne bakabilirsiniz.

## İpuçları
*   **Permission Denied:** Eğer bu hatayı alırsanız komutun başına `sg docker -c` eklemeyi unutmayın.
*   **ROS Komutları:** `ros2` ile başlayan tüm komutlar sadece 2. terminalde (source yapıldıktan sonra) çalışır.
