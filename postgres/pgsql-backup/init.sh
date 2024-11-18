set -e

echo '* libraries/restart-without-asking boolean true' | sudo debconf-set-selections
TZ=Asia/Almaty
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
sudo locale-gen en_US.UTF-8

apt update
apt install -y lsb-release gnupg2

sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -

sudo apt-get update
sudo apt-get -y install postgresql
service postgresql start

curl -sLO https://stepik.org/media/attachments/lesson/702368/dump.sql
sudo -iu postgres psql -U postgres -c "create database deadline"
sudo -iu postgres psql -U postgres deadline < dump.sql
sudo rm -f dump.sql

sudo -iu postgres psql -U postgres -c "create user murat with encrypted password 'mypass';\
    create user serik with encrypted password 'mypass';\
    create user steve with encrypted password 'mypass';"

