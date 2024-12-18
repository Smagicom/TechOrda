#!/bin/bash
sudo docker run -d --name jusan-docker-exec -p 8181:80 nginx:mainline
sudo docker exec -it jusan-docker-exec bash
curl http://localhost:8181
curl http://localhost:8181/home
curl http://localhost:8181/about
sudo docker logs jusan-docker-exec

cd /etc/nginx/conf.d/
nano jusan-docker-exec.conf
cat << EOF > /etc/nginx/conf.d/jusan-docker-exec.conf
server {
    listen 80;
    server_name jusan.singularity;

    location / {return 200 'Hello, from jusan-docker-exec';}
    location /home {return 201 'This is my home!';}
    location /about {return 202 'I am just an exercise!';}
}
EOF

cat jusan-docker-exec.conf
rm default.conf 
nginx -s reload
