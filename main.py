from flask import Flask, render_template, url_for, request, json
from util import json_response, check_existing_username
import persistence
import data_handler

app = Flask(__name__)


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
    return data_handler.get_boards()


@app.route("/get-cards/<int:board_id>")
@json_response
def get_cards_for_board(board_id: int):
    """
    All cards that belongs to a board
    :param board_id: id of the parent board
    """
    return data_handler.get_cards_for_board(board_id)


@app.route('/registration', methods=['POST'])
def registration():
    if request.method == 'POST':
        try:
            data = json.loads(request.data)
            username = data['username']
            password_first = data['passwordFirst']
            password_second = data['passwordSecond']
            if password_first == password_second and check_existing_username:
                persistence.registrate_user(username, password_first)
            else:
        except:
            print('valami')


@app.route('/login', methods=['GET', 'POST'])
def login():
    user_name = request.form['username']
    password = request.form['password']
    try:
        good_password_hash = persistence.get_good_hash_by_user_name(user_name)
        if util.verify_password(password, good_password_hash):
            session['username'] = user_name
            return redirect('/')
        else:
            return 'invalid username or password'
    except IndexError:
        return "invalid username or password"


def main():
    app.run(debug=True)

    # Serving the favicon
    with app.app_context():
        app.add_url_rule('/favicon.ico', redirect_to=url_for('static', filename='favicon/favicon.ico'))


if __name__ == '__main__':
    main()
