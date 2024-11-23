SOLUTION = [
    'deadline',
    'deadline_type',
    'module',
    'schema_migrations',
    'student',
    'student_deadline',
]

def check(reply):
    if not reply:
        return False
    names = [name.strip() for name in reply.split('\n')]
    return sorted(names) == sorted(SOLUTION)
