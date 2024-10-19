import re

patterns = [
    r"deny\s+192.0.0.1",
    r"deny\s+all",
    r"allow\s+192.0.0.1\/20",
]

def check(reply):
    for pattern in patterns:
        matches = re.search(pattern, reply)
        if matches is None:
            return False, "incorrect rules"
    return True
