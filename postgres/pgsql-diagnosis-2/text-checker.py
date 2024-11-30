SOLUTION = [
    'murat',
    'postgres',
    'serik',
    'steve',
]

def check(reply):
    if not reply:
        return False
    names = [name.strip() for name in reply.split('\n')]
    return sorted(names) == sorted(SOLUTION)
