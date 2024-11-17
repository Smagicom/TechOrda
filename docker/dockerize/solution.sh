 curl -O https://raw.githubusercontent.com/Rinotrihanna/TechOrda/main/docker/dockerize/fastapi-final/Dockerfile
 curl -O https://raw.githubusercontent.com/Rinotrihanna/TechOrda/main/docker/dockerize/fastapi-final/requirements.txt
 docker build -t jusan-fastapi-final:dockerized .
 docker images
 docker run -d -p 8080:8080 --name jusan-dockerize jusan-fastapi-final:dockerized

