CHECK_QUERY="select id, name, age, country, department from users where id=4"
REQUIRED_ROW=(4, 'azatmukanov', 40, 'GER', 'operations')

def check(query, result):
    if "insert" not in query.lower():
        return False, "Используйте операцию INSERT, чтобы вносить данные."
    count = cursor.execute(CHECK_QUERY)
    if cursor.fetchone() == REQUIRED_ROW:
        return True
    if count == 0:
        return False, "Требуемая запись не найдена."
    return False, "Записанные данные не соответстуют задаче."
