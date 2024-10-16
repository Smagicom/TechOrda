patterns = [
    ("ufw allow 'Nginx HTTP'", "ufw allow 'Nginx HTTPS'"),
    ("ufw allow 'Nginx Full'"),
    ("ufw allow 80/tcp", "ufw allow 443/tcp"),
]

def check(reply):
    checked = False
    for rules in patterns:
        every = True
        for rule in rules:
            if rule not in reply:
                every = False
                break
        if every:
            checked = True

    if not checked:
        return False, "ports are not allowed"
    if "ufw enable" not in reply:
        return False, "ufw is not enabled!"
    return True
