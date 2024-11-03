# nginx-ufw

На вашем сервере может быть запущено несколько сервисов помимо nginx. Оставлять доступ к ним открытым из Интернета может быть очень опасно.
Злоумышленники могут этим воспользоваться и взломать один из открытых сервисов.

Для безопасности, нужно закрыть к ним доступы и оставить только доступ к веб-серверу nginx. Одним из способов это сделать является команда `ufw`.

На данном уроке, мы научимся как обезопасить свой сервер.

### Полезные ссылки

- [UFW - Uncomplicated Firewall](https://help.ubuntu.com/community/UFW)
- [Hello Linux: Nginx & UFW Firewall](https://www.codingforentrepreneurs.com/blog/hello-linux-nginx-and-ufw-firewall)

### Задание

1. На своем компьютере запустите nginx. Скачайте `ufw` и настройте доступ извне только на порты 80 и 443.
2. Отправьте выполненные команды.

---

### Ответ
sudo apt update 
sudo apt install ufw
sudo ufw disable 
sudo ufw allow ssh
sudo ufw allow 'Nginx Full'
sudo ufw enable
sudo ufw status verbose

Status: active
Logging: on (low)
Default: deny (incoming), allow (outgoing), deny (routed)
New profiles: skip

To                         Action      From
--                         ------      ----
22/tcp                     ALLOW IN    Anywhere                  
80,443/tcp (Nginx Full)    ALLOW IN    Anywhere                  
22/tcp (v6)                ALLOW IN    Anywhere (v6)             
80,443/tcp (Nginx Full (v6)) ALLOW IN    Anywhere (v6)    

