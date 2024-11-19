AFFECTED_ROWS=2
COLUMNS=['name', 'age', 'department']
ROWS=[
    ['bumirbayev', 25, 'education'],
    ['armanakmetov', 23, 'development'],
]

def check(query, result):
    if "select" not in query.lower():
        return False, "Используйте операцию SELECT, чтобы вытаскивать данные."
    if result['affected_rows'] != AFFECTED_ROWS:
        return False, "Запрос должен содержать кол-во строк: {}.".format(AFFECTED_ROWS)
    if result['columns'] != COLUMNS:
        return False, "Неверное кол-во колонок, либо порядок, либо названия колонок."
    if sorted(result['rows']) != sorted(ROWS):
        return False, "Получены не те строки"
    return True
