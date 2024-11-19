echo '* libraries/restart-without-asking boolean true' | sudo debconf-set-selections

apt update
apt install -y lsb-release gnupg2 unzip apt-transport-https

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

curl -1sLf "https://keys.openpgp.org/vks/v1/by-fingerprint/0A9AF2115F4687BD29803A206B73A36E6026DFCA" | sudo gpg --dearmor | sudo tee /usr/share/keyrings/com.rabbitmq.team.gpg > /dev/null
curl -1sLf https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/gpg.E495BB49CC4BBE5B.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/io.cloudsmith.rabbitmq.E495BB49CC4BBE5B.gpg > /dev/null
curl -1sLf https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-server/gpg.9F4587F226208342.key | sudo gpg --dearmor | sudo tee /usr/share/keyrings/io.cloudsmith.rabbitmq.9F4587F226208342.gpg > /dev/null


sudo tee /etc/apt/sources.list.d/rabbitmq.list <<EOF
deb [signed-by=/usr/share/keyrings/io.cloudsmith.rabbitmq.E495BB49CC4BBE5B.gpg] https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/deb/ubuntu bionic main
deb-src [signed-by=/usr/share/keyrings/io.cloudsmith.rabbitmq.E495BB49CC4BBE5B.gpg] https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-erlang/deb/ubuntu bionic main
deb [signed-by=/usr/share/keyrings/io.cloudsmith.rabbitmq.9F4587F226208342.gpg] https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-server/deb/ubuntu bionic main
deb-src [signed-by=/usr/share/keyrings/io.cloudsmith.rabbitmq.9F4587F226208342.gpg] https://dl.cloudsmith.io/public/rabbitmq/rabbitmq-server/deb/ubuntu bionic main
EOF

sudo apt-get update -y

sudo apt-get install -y erlang-base \
                        erlang-asn1 erlang-crypto erlang-eldap erlang-ftp erlang-inets \
                        erlang-mnesia erlang-os-mon erlang-parsetools erlang-public-key \
                        erlang-runtime-tools erlang-snmp erlang-ssl \
                        erlang-syntax-tools erlang-tftp erlang-tools erlang-xmerl

sudo apt-get install rabbitmq-server -y --fix-missing

sudo rabbitmq-plugins enable rabbitmq_management

sudo systemctl start rabbitmq-server
