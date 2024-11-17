root@user-asus:/etc/nginx# cat ./sites-available/default
server {
    listen 8080;
    server_name example.com;

    location /secret_word {
        # Возвращает строку jusan-nginx-ip со статусом 203
        return 203 "jusan-nginx-ip";

        # Разрешение доступа из диапазона 192.0.0.0/20, кроме 192.0.0.1
        allow 192.0.0.0/20;
        deny 192.0.0.1;
        
        # Запрет для всех остальных
        deny all;

        # Установка заголовка Content-Type
        add_header Content-Type text/plain;

    }

    location / {
        root /var/www/html;  # Путь к index.html
        index index.html;
    }

    location /images {
        auth_basic "Protected Area for Design";
        auth_basic_user_file /etc/nginx/conf.d/passwd;
        # Разархивируйте cats.zip в /var/www/html/cats
        alias /var/www/html/cats;
        autoindex on;
    }

    location /gifs {
        auth_basic "Protected Area for Marketing";
        auth_basic_user_file /etc/nginx/conf.d/passwd;
        # Разархивируйте gifs.zip в /var/www/html/gifs
        alias /var/www/html/gifs;
        autoindex on;
    }

    # Запрет на доступ к другим путям для учетной записи design
    location /restricted_design {
        satisfy any;
        deny all;
    }

    # Запрет на доступ к другим путям для учетной записи marketing
    location /restricted_marketing {
        satisfy any;
        deny all;
    }
}
root@user-asus:/etc/nginx# nano ./sites-available/default
root@user-asus:/etc/nginx# nginx -t
nginx: [warn] conflicting server name "example.com" on 0.0.0.0:8080, ignored
nginx: [warn] conflicting server name "jusan.kz" on 0.0.0.0:443, ignored
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful
root@user-asus:/etc/nginx# systemctl restart nginx
root@user-asus:/etc/nginx# curl --user marketing:marketingP@ssword http://localhost:8080/gifs/
<html>
<head><title>Index of /gifs/</title></head>
<body>
<h1>Index of /gifs/</h1><hr><pre><a href="../">../</a>
<a href="__MACOSX/">__MACOSX/</a>                                          27-Oct-2024 14:06                   -
<a href="dancing.gif">dancing.gif</a>                                        25-Mar-2022 11:20              253794
<a href="jam.gif">jam.gif</a>                                            25-Mar-2022 11:20              471720
<a href="sad.gif">sad.gif</a>                                            25-Mar-2022 11:21             3605836
</pre><hr></body>
</html>
