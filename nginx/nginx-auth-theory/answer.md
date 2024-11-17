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
