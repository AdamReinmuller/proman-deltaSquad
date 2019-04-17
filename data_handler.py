import persistence


def get_card_status(status_id):
    """
    Find the first status matching the given id
    :param status_id:
    :return: str
    """
    statuses = persistence.get_statuses()
    return next((status['title'] for status in statuses if str(status['id']) == str(status_id)), 'Unknown')


def get_statuses():
    asd = persistence.get_statuses()
    return asd


def get_boards():
    """
    Gather all boards
    :return:
    """
    return persistence.get_all_boards()


def get_cards_for_board(board_id):
    persistence.clear_cache()
    all_cards = persistence.get_all_cards()
    matching_cards = []
    for card in all_cards:
        if str(card['board_id']) == str(board_id):
            card['status_id'] = get_card_status(card['status_id'])  # Set textual status for the card
            matching_cards.append(card)
    return matching_cards
