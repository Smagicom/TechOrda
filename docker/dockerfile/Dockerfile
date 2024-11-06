FROM nginx:mainline
WORKDIR /var/www
COPY jusan-dockerfile.conf /etc/nginx/conf.d/jusan-dockerfile.conf
COPY jusan-dockerfile .
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]