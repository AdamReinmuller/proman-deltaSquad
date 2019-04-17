import connection
from psycopg2 import sql
import util

STATUSES_FILE = './data/statuses.csv'
BOARDS_FILE = './data/boards.csv'
CARDS_FILE = './data/cards.csv'

_cache = {}  # We store cached data in this dict to avoid multiple file readings


def clear_cache():
    for k in list(_cache.keys()):
        _cache.pop(k)


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
        cursor.execute('''INSERT INTO cards (board_id, title, status_id, order_number) 
        VALUES (%(board_id)s, %(title)s, %(status)s, %(order)s);''',
                       {'board_id': board_id, 'title': title, 'status': status_id, 'order': order_number + 1})
    else:
        cursor.execute(
            '''INSERT INTO cards (board_id, title, status_id, order_number) VALUES (%(board_id)s, %(title)s, %(status)s, 0);''',
            {'board_id': board_id, 'title': title, 'status': status_id})


@connection.connection_handler
def add_new_board(cursor):
    cursor.execute("""
    INSERT INTO boards (title)
    VALUES (%(defaultTitle)s);
    """,
                   {'defaultTitle': "New board"})


@connection.connection_handler
def add_new_private_board(cursor, user):
    cursor.execute("""
    INSERT INTO boards (title)
    VALUES (%(defaultTitle)s);
    """,
                   {'defaultTitle': "New board"})


@connection.connection_handler
def get_board_by_ID(cursor, boardID):
    cursor.execute("""
    SELECT * FROM boards 
    JOIN cards ON boards.id = cards.board_id
    JOIN statuses ON cards.status_id = statuses.id
    WHERE boards.id=%(boardID)s;
    """,
                   {'boardID': boardID})

    return cursor.fetchall()


@connection.connection_handler
def get_all_boards(cursor):
    cursor.execute("""
    SELECT * FROM boards 
    """)

    return cursor.fetchall()


def get_card_by_id(cursor, cardID):
    cursor.execute("""
    SELECT * FROM cards
    WHERE cards.id = %(cardID)s;
    """,
                   {'cardID': cardID})

    return cursor.fetchone()


@connection.connection_handler
def get_cards_by_boardID(cursor, boardID):
    cursor.execute("""
    SELECT * FROM cards 
    WHERE board_id=%(board_id)s;
    """,
                   {'board_id': boardID})

    return cursor.fetchall()


@connection.connection_handler
def delete_card(cursor, cardID):
    cursor.execute("""
    DELETE FROM cards 
    WHERE id=%(card_id);
    """,
                   {'card_id': cardID})


@connection.connection_handler
def delete_board(cursor, boardID):
    cursor.execute("""
    DELETE FROM cards 
    WHERE cards.board_id=%(boardID);
    DELETE FROM boards
    WHERE boards.id=%(boardID);
    """,
                   {'boardID': boardID})


@connection.connection_handler
def edit_board_name(cursor, boardID, newName):
    cursor.execute("""
        UPDATE boards 
        SET boards.title = %(newName)s
        WHERE id=%(boardID)s;
        """,
                   {'boardID': boardID, 'newName': newName}
                   )


@connection.connection_handler
def get_statuses(cursor):
    cursor.execute("""
    SELECT * FROM statuses 
    """)

    return cursor.fetchall()


@connection.connection_handler
def get_all_cards(cursor):
    cursor.execute("""
    SELECT * FROM cards 
    """)

    return cursor.fetchall()
