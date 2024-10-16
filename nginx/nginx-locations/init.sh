set -e

echo '* libraries/restart-without-asking boolean true' | sudo debconf-set-selections

apt update
apt install -y unzip gnupg2

cat << EOF >/etc/apt/sources.list.d/nginx.list
deb http://nginx.org/packages/mainline/ubuntu/ bionic nginx
deb-src http://nginx.org/packages/mainline/ubuntu/ bionic nginx
EOF

curl -sLO http://nginx.org/keys/nginx_signing.key && apt-key add nginx_signing.key

apt update && apt install -y nginx
service nginx start
