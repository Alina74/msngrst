import sqlite3


def get_user_id():

    uri = 'db.sqlite'
    query = 'SELECT 1'

    with sqlite3.connect(uri) as connection:
        cursor = connection.execute(query)

    row = cursor.fetchone()

    return row


if __name__ == '__main__':

    user_id = get_user_id()
    print(user_id)

