openssl req -x509 -nodes -days 1825 -newkey rsa:2048 \
	-keyout ./track-devops.key \
	-out ./track-devops.crt
