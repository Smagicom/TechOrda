set -e

echo '* libraries/restart-without-asking boolean true' | sudo debconf-set-selections

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

rm -rf "$UNPACKED_DIRECTORY"
