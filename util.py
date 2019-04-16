from functools import wraps
from flask import jsonify
import connection

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
                      LIMIT 1;''', {'board_id':board_id, 'title':title})
    order_number = cursor.fetchone()['order_number']
    return order_number

if __name__ == '__main__':
    print(set_card_order(1, 'done card'))
