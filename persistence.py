import csv
import connection

from psycopg2 import sql
import util

STATUSES_FILE = './data/statuses.csv'
BOARDS_FILE = './data/boards.csv'
CARDS_FILE = './data/cards.csv'

_cache = {}  # We store cached data in this dict to avoid multiple file readings


def _read_csv(file_name):
    """
    Reads content of a .csv file
    :param file_name: relative path to data file
    :return: OrderedDict
    """
    with open(file_name) as boards:
        rows = csv.DictReader(boards, delimiter=',', quotechar='"')
        formatted_data = []
        for row in rows:
            formatted_data.append(dict(row))
        return formatted_data


def get_board_by_ID(cursor, boardID):
    cursor.execute("""
    SELECT * FROM boards 
    JOIN cards ON boards.id = cards.board_id
    JOIN statuses ON cards.status_id = statuses.id
    WHERE boards.id=%(boardID)s;
    """,
                   {'boardID': boardID})

    return cursor.fetchall()


def get_all_boards(cursor):
    cursor.execute("""
    SELECT * FROM boards 
    JOIN cards ON boards.id = cards.board_id
    JOIN statuses ON cards.status_id = statuses.id;
    """)

    return cursor.fetchall()


def get_card_by_id(cursor, cardID):
    cursor.execute("""
    SELECT * FROM cards
    WHERE cards.id = %(cardID)s;
    """,
                   {'cardID': cardID})

    return cursor.fetchone()


def get_cards_by_boardID_and_statusID(cursor, boardID, statusID):
    cursor.execute("""
    SELECT * FROM cards 
    WHERE board_id=%(board_id)s AND status_id=%(statusID)s;
    """,
                   {'board_id': boardID, 'status_id': statusID})

    return cursor.fetchall()


def delete_card(cursor, cardID):
    cursor.execute("""
    DELETE FROM cards 
    WHERE id=%(card_id);
    """,
                   {'card_id': cardID})


def delete_board(cursor, boardID):
    cursor.execute("""
    DELETE FROM cards 
    WHERE cards.board_id=%(boardID);
    DELETE FROM boards
    WHERE boards.id=%(boardID);
    """,
                   {'boardID': boardID})


def edit_board_name(cursor, boardID, newName):
    cursor.execute("""
        UPDATE boards 
        SET boards.title = %(newName)
        WHERE id=%(boardID)s;
        """,
                   {'boardID': boardID, 'newName': newName}
                   )

