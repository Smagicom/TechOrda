set -x

echo '* libraries/restart-without-asking boolean true' | sudo debconf-set-selections
TZ=Asia/Almaty
ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
sudo locale-gen en_US.UTF-8

apt update
apt install -y lsb-release gnupg2 unzip

VERSION="1.5.4505"
SYSTEMCTL_NAME="docker-systemctl-replacement"

URL_ARCHIVE="https://github.com/gdraheim/docker-systemctl-replacement/archive/refs/tags/v1.5.4505.zip"
ARCHIVE_NAME="$SYSTEMCTL_NAME.zip"
UNPACKED_DIRECTORY="$SYSTEMCTL_NAME-$VERSION"

curl -sL -o $ARCHIVE_NAME $URL_ARCHIVE
unzip $ARCHIVE_NAME > /dev/null

mv "$UNPACKED_DIRECTORY/files/docker/journalctl3.py" /usr/bin/journalctl
mv "$UNPACKED_DIRECTORY/files/docker/systemctl3.py" /usr/bin/systemctl
chmod 755 /usr/bin/systemctl /usr/bin/journalctl

rm -rf "$UNPACKED_DIRECTORY" "$ARCHIVE_NAME"

apt update
curl -sL https://www.mongodb.org/static/pgp/server-5.0.asc | apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/5.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-5.0.list

apt update
apt install -y mongodb-org
systemctl start mongod
sleep 3

mongo << EOF
use admin
db.createUser(
  {
    user: "admin",
    pwd: "singularity",
    roles: [ { role: 'root', db: 'admin' } ]
  }
)
EOF
