from flask_login import FlaskLoginClient
from app import User, db


def test_check_account_balance(application):
    """ Testing account balance """
    """ Making user account """
    application.test_client_class = FlaskLoginClient
    user = User('hss56@njit.edu', 'testpass', 1)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'hss56@njit.edu'
    assert user.balance == 0


def test_calculate_account_balance(application):
    """ Testing account balance """
    """ Making user account """
    application.test_client_class = FlaskLoginClient
    user = User('hss56@njit.edu', 'testpass', 1)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'hss56@njit.edu'
    assert user.balance == 0

    user.balance += 3500
    assert user.balance == 3500

    user.balance += 399
    assert user.balance == 3899

    user.balance -= 1800
    assert user.balance == 2099

    user.balance -= 99
    assert user.balance == 2000
