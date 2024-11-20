#!/bin/bash
sudo docker run -d --name jusan-docker-bind -p 7777:80 -v /home/sbeissov/nginx.conf:/etc/nginx/nginx.conf nginx:mainline

sudo docker ps

sudo docker logs jusan-docker-bind
