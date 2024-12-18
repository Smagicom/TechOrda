#!/bin/bash
sudo docker run -d --name jsn-dkr-run -p 8888:80 nginx:mainline
sudo docker ps
docker stop jsn-dkr-run
sudo docker ps
sudo docker ps -a