import os
from flask_login import FlaskLoginClient
from app import config, db, User
from app.account_transactions import csv_upload


# using the link below Flask-Login provides a simple, custom test client class that will set the user’s login cookie
# https://flask-login.readthedocs.io/en/latest/#automated-testing


def test_upload_csv_denied(application):
    """ Trying to upload music.cvs without being logged in - denied """
    application.test_client_class = FlaskLoginClient
    # no user in session = no user logged in
    assert db.session.query(User).count() == 0
    with application.test_client(user=None) as client:
        response = client.get('/account_transactions/upload')
        assert response.status_code == 302
        base_path = config.Config.BASE_DIR
        transactions_file = os.path.join(base_path, '../transactions.csv')
        form = csv_upload()
        form.file = transactions_file
        assert form.validate


def test_upload_csv_success(application):
    """ Trying to upload music.cvs with a logged-in user - success """
    application.test_client_class = FlaskLoginClient
    user = User('hss56@njit.edu', 'testpass', 1)
    db.session.add(user)
    db.session.commit()
    assert user.email == 'hss56@njit.edu'
    assert db.session.query(User).count() == 1

    base_path = config.Config.BASE_DIR
    transactions_file = os.path.join(base_path, '../transactions.csv')

    with application.test_client(user=user) as client:
        response = client.get('/account_transactions/upload')
        assert response.status_code == 200
        form = csv_upload()
        form.file = transactions_file
        assert form.validate
