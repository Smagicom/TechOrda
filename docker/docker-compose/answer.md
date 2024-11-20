<code>root@user-asus:/home/user/Documents/jusan-docker/docker-compose# docker-compose up -d
Creating network "docker-compose_default" with the default driver
Creating jusan-compose ... done
root@user-asus:/home/user/Documents/jusan-docker/docker-compose# docker ps
CONTAINER ID   IMAGE                            COMMAND                  CREATED          STATUS                         PORTS     NAMES
786cae00cc10   jusan-fastapi-final:dockerized   "uvicorn main:app --…"   14 seconds ago   Restarting (1) 3 seconds ago             jusan-compose
root@user-asus:/home/user/Documents/jusan-docker/docker-compose# </code>
