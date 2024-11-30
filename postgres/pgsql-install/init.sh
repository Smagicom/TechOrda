set -e

echo '* libraries/restart-without-asking boolean true' | sudo debconf-set-selections

apt update
apt install -y lsb-release gnupg2
