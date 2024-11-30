def test_users(s):
    credentials = [
        ("administrator", "Lhc9kkVV"),
        ("app-developer", "9cDtdMTj"),
        ("guest", "GmBtuC5X"),
    ]
    cmd = "rabbitmqctl authenticate_user {} {}"
    for user, password in credentials:
        stdout = s.run(cmd.format(user, password))
        assert stdout.succeeded, user + " is incorrectly configured."

def test_permissions(s):
    permissions = [
        "administrator",
        "app-developer",
    ]
    cmd = 'rabbitmqctl list_permissions -s -p application | grep {}'
    for p in permissions:
        stdout = s.run(cmd.format(p))
        assert stdout.count(".\*") == 3, p + " has incorrect permissions."
