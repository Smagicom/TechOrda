set -e

echo '* libraries/restart-without-asking boolean true' | sudo debconf-set-selections

# api
curl -o /tmp/api -sL https://github.com/alem-io/track-devops-systemd-api/releases/download/v0.1/api
chmod 755 /tmp/api
nohup /tmp/api &

# nginx
apt update
apt install -y gnupg2 unzip

cat << EOF >/etc/apt/sources.list.d/nginx.list
deb http://nginx.org/packages/mainline/ubuntu/ bionic nginx
deb-src http://nginx.org/packages/mainline/ubuntu/ bionic nginx
EOF

curl -sLO http://nginx.org/keys/nginx_signing.key && apt-key add nginx_signing.key

apt update && apt install -y nginx
service nginx start
