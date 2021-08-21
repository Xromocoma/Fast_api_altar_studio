from app.database import db
from app.models import Login


def get_all_users():
    sql = {}

    sql.cursor.execute("""SELECT id, name, role FROM user;""")
    res = sql.cursor.fetchall()
    result = []
    if res:
        for item in res:
            result.append({"id": item[0],
                           "name": item[1],
                           "role": item[2]})

    return result


def update_user(role, name, user_id):
    try:
        sql = {}
        query = f"update user set role = {role}, name = {name}  WHERE id = {user_id}"
        sql.cursor.execute(query)
        sql.connection.commit()
    except BaseException as e:
        return e
    return None


def delete_user(user_id):
    try:
        sql = {}
        query = f"DELETE user WHERE id = {user_id}"
        sql.cursor.execute(query)
        sql.connection.commit()
    except BaseException as e:
        return e
    return None


def insert_user(raw):
    try:
        sql = {}
        sql.cursor.execute("SELECT max(id) FROM user;")
        max_id = sql.cursor.fetchone()
        print(max_id)
        max_id += 1
        query = f"insert into user values ({max_id},?,?,?,?)"
        sql.cursor.execute(query, raw)
        sql.connection.commit()
    except BaseException as e:
        return e
    return None


async def user_login(Login):
    return True
