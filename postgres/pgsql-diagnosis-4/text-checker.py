SOLUTION = [
    'id',
    'student_id',
    'deadline_id',
    'module_id',
    'index',
    'duration',
    'is_success',
    'started_at',
    'created_at',
    'updated_at',
]

def check(reply):
    if not reply:
        return False
    names = [name.strip() for name in reply.split('\n')]
    return sorted(names) == sorted(SOLUTION)
