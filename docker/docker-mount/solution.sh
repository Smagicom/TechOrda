#!/bin/bash
sudo docker run -d --name jusan-docker-mount -p 9988:80 -v /home/sbeissov/github/TechOrda/docker/docker-mount/jusan-docker-mount.conf:/etc/nginx/conf.d/nginx.conf -v /home/sbeissov/github/TechOrda/docker/docker-mount/jusan-docker-mount:/usr/share/nginx/html nginx:mainline
