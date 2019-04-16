import connection
from psycopg2 import sql
import util

STATUSES_FILE = './data/statuses.csv'
BOARDS_FILE = './data/boards.csv'
CARDS_FILE = './data/cards.csv'

_cache = {}  # We store cached data in this dict to avoid multiple file readings


@connection.connection_handler
def read_database_table(cursor, db_table):
    """
    Reads content from a database-table
    :param file_name: relative path to data file
    :return: OrderedDict
    """
    cursor.execute(sql.SQL('''SELECT *
                              FROM {database_name};''').format(database_name=sql.Identifier(db_table)))
    data = cursor.fetchall()
    return data


@connection.connection_handler
def insert_new_card(cursor, board_id, title, status_id):
    order_number = util.set_card_order(board_id, title)
    if order_number:
        cursor.execute('''INSERT INTO cards (board_id, title, status_id, order_number) VALUES (%(board_id)s, %(title)s, %(status)s, %(order)s);''',
                       {'board_id':board_id, 'title':title, 'status':status_id, 'order':order_number+1})
    else:
        cursor.execute('''INSERT INTO cards (board_id, title, status_id, order_number) VALUES (%(board_id)s, %(title)s, %(status)s, 0);''',
                       {'board_id': board_id, 'title': title, 'status': status_id})
