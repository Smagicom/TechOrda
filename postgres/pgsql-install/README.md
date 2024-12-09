# pgsql-install

### Полезное

- [Download PostgreSQL Ubuntu](https://www.postgresql.org/download/linux/ubuntu/)

### Задание

1. Установить и запустить на удаленном сервере stepik наиболее актуальную версию `postgresql`.

---

### Ответ

```Postgres
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget -qO - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
sudo apt update
sudo apt install postgresql postgresql-contrib -y
sudo systemctl start postgresql
sudo systemctl enable postgresql
sudo -u postgres psql
\l


```
