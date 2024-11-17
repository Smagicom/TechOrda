> root@user-asus:/etc/nginx# ufw allow 80/tcp
> Skipping adding existing rule
> Skipping adding existing rule (v6)
> root@user-asus:/etc/nginx# ufw allow 443/tcp
> Skipping adding existing rule
> Skipping adding existing rule (v6)
> root@user-asus:/etc/nginx# ufw status
> Status: active

To                         Action      From
--                         ------      ----
22                         ALLOW       Anywhere                  
22/tcp                     ALLOW       Anywhere                  
2222/tcp                   ALLOW       Anywhere                  
80/tcp                     ALLOW       Anywhere                  
443/tcp                    ALLOW       Anywhere                  
22 (v6)                    ALLOW       Anywhere (v6)             
22/tcp (v6)                ALLOW       Anywhere (v6)             
2222/tcp (v6)              ALLOW       Anywhere (v6)             
80/tcp (v6)                ALLOW       Anywhere (v6)             
443/tcp (v6)               ALLOW       Anywhere (v6)             


