#!/bin/bash
xhost +local:root
XSOCK=/tmp/.X11-unix

# Create local data directory if not exists
mkdir -p /home/momererkoc/Desktop/LunarSim/data

docker rm -f lunarsim 2>/dev/null

docker run -it \
 --runtime=nvidia \
 --gpus all \
 -e DISPLAY=$DISPLAY \
 -v $XSOCK:$XSOCK \
 -v $HOME/.Xauthority:/root/.Xauthority \
 -v /home/momererkoc/Desktop/LunarSim/data:/root/lunarsim/data \
 --privileged \
 --net=host \
 --name=lunarsim \
 lunarsim:latest bash
