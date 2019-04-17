from flask import Flask, render_template, url_for, request, session, redirect
from util import json_response, check_existing_username, verify_password, get_good_hash_by_user_name
import persistence
import data_handler

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route("/")
def index():
    """
    This is a one-pager which shows all the boards and cards
    """
    return render_template('index.html')


@app.route("/get-boards")
@json_response
def get_boards():
    """
    All the boards
    """
    asd = data_handler.get_boards()
    return asd


# @app.route("/get-statuses")
# @json_response
# def get_statuses(status_id: int):
#     """
#     Get all status
#     """
#     return data_handler.get_statuses()


@app.route("/get-statuses/<status_id>")
@json_response
def get_status(status_id: int):
    """
    Get status
    """
    return data_handler.get_card_status(status_id)


@app.route("/get-cards/<int:board_id>")
@json_response
def get_cards_for_board(board_id: int):
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """
    return data_handler.get_cards_for_board(board_id)


@app.route('/registration', methods=['POST'])
@json_response
def registration():
    if request.method == 'POST':
        try:
            data = request.form
            username = data['username']
            password_first = data['password_1']
            password_second = data['password_2']
            if password_first == password_second:
                if not check_existing_username(username):
                    persistence.registrate_user(username, password_first)
                else:
                    data = {'response': 'username already exists'}
                    return data

            else:
                data = {'response': 'passwords does not match'}
                return data
        except:
            data = {'response': 'something went wrong :( '}
            return data


@app.route('/login', methods=['POST'])
@json_response
def login():
    user_name = request.form['username']
    password = request.form['password']
    try:
        good_password_hash = get_good_hash_by_user_name(user_name)
        if verify_password(password, good_password_hash):
            session['username'] = user_name
        else:
            data = {'response': 'invalid username or password'}
            return data
    except IndexError:
        data = {'response': 'invalid username or password'}
        return data


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
