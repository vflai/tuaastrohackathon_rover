#!/bin/bash

# GUI Izni
xhost +local:root
XSOCK=/tmp/.X11-unix

cleanup() {
    echo -e "\n--- SİSTEM KAPATILIYOR ---"
    sg docker -c "docker exec lunarsim pkill -9 -f LunarSim" 2>/dev/null || true
    sg docker -c "docker exec lunarsim pkill -9 -f python3" 2>/dev/null || true
    sg docker -c "docker rm -f lunarsim" 2>/dev/null || true
    exit
}
trap cleanup SIGINT

echo "--- SİSTEM SIFIRLANIYOR ---"
sg docker -c "docker rm -f lunarsim 2>/dev/null" || true
sleep 1

echo "--- LUNAR MISSION MASTER V31 (IRON DOME) ---"

# 1. Konteynırı Başlat
sg docker -c "docker run -dt --runtime=nvidia --gpus all -e DISPLAY=$DISPLAY -v $XSOCK:$XSOCK -v $HOME/.Xauthority:/root/.Xauthority -v /home/momererkoc/Desktop/LunarSim/data:/root/lunarsim/data --privileged --net=host --name=lunarsim lunarsim:latest bash"
sleep 2

# 2. LunarSim
echo "[1/5] Simülatör Başlatılıyor..."
sg docker -c "docker exec -d lunarsim bash -c './LunarSim.x86_64'"
sleep 15

# 3. Altyapı (TF ve Onarım)
echo "[2/5] TF ve Veri Onarımı..."
sg docker -c "docker exec -d lunarsim bash -c 'source /opt/ros/humble/setup.bash && cd /root/lunarsim/data && python3 header_repair.py'"

# 4. 3D Görüntü (RViz İçin)
echo "[3/5] 3D Harita Yayını (PointCloud)..."
sg docker -c "docker exec -d lunarsim bash -c 'source /opt/ros/humble/setup.bash && cd /root/lunarsim/data && python3 depth_to_pc.py'"

# 5. Navigasyon Beyni (CANLI LOGLAR TERMİNALDE)
echo "[4/5] Navigasyon Beyni Başlatılıyor..."
echo "------------------------------------------------------------"
sg docker -c "docker exec lunarsim bash -c 'source /opt/ros/humble/setup.bash && cd /root/lunarsim/data && python3 lunar_planner.py'" &

# 6. RViz
echo "[5/5] RViz Açılıyor..."
sg docker -c "docker exec -it lunarsim bash -c 'source /opt/ros/humble/setup.bash && rviz2 -d /root/lunarsim/data/lunar_config.rviz'"
