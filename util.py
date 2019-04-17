from functools import wraps
from flask import jsonify
import connection
import bcrypt


def json_response(func):
    """
    Converts the returned dictionary into a JSON response
    :param func:
    :return:
    """

    @wraps(func)
    def decorated_function(*args, **kwargs):
        return jsonify(func(*args, **kwargs))

    return decorated_function


@connection.connection_handler
def set_card_order(cursor, board_id, title):
    cursor.execute('''SELECT order_number FROM cards
                      WHERE board_id = %(board_id)s AND title = %(title)s
                      ORDER BY order_number DESC
                      LIMIT 1;''', {'board_id': board_id, 'title': title})
    order_number = cursor.fetchone()['order_number']
    return order_number


@connection.connection_handler
def get_good_hash_by_user_name(cursor, user_name):
    cursor.execute('''SELECT hashed_pw FROM users WHERE user_name = %(user_name)s''', {'user_name': user_name})
    password_hash = cursor.fetchall()[0]['password_hash']
    return password_hash


@connection.connection_handler
def check_existing_username(cursor, username):
    cursor.execute('''SELECT * FROM users
                      WHERE user_name = %(username)s''', {'username': username})
    result = cursor.fetchall()
    return result


def hash_password(plain_text_password):
    # By using bcrypt, the salt is saved into the hash itself
    hashed_bytes = bcrypt.hashpw(plain_text_password.encode('utf-8'), bcrypt.gensalt())
    return hashed_bytes.decode('utf-8')


def verify_password(plain_text_password, hashed_password):
    hashed_bytes_password = hashed_password.encode('utf-8')
    value = bcrypt.checkpw(plain_text_password.encode('utf-8'), hashed_bytes_password)
    return value


if __name__ == '__main__':
    print(set_card_order(1, 'done card'))
