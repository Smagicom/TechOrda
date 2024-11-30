CHECK_QUERY="select 1 from users where id=2"

def check(query, result):
    if "delete" not in query.lower():
        return False, "Используйте операцию DELETE, чтобы удалять записи."
    count = cursor.execute(CHECK_QUERY)
    if count != 0:
        return False, "Требуемая запись не удалена."
    return True
