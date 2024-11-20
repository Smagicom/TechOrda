#!/bin/bash
sudo docker build -t jusan-fastapi-final:dockerized .

sudo docker run -d -p 8080:8080 --name jusan-dockerize jusan-fastapi-final:dockerized