location /api {
    proxy_pass http://localhost:9090;
    rewrite ^/api(/.*)?$ $1 break;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    add_header web-server 0;
}




