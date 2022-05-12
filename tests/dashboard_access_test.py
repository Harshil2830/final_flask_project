from flask_login import FlaskLoginClient

from app import User, db


def test_dashboard_denied(client):
    """ Test to get dashboard denied """
    response = client.get("/dashboard")
    assert response.status_code == 302


def test_dashboard_success(application):
    """ Test to retrieve dashboard """
    application.test_client_class = FlaskLoginClient
    user = User('hss56@njit.edu', 'testpass', 1)
    db.session.add(user)
    db.session.commit()
    # user is logged in
    assert user.email == 'hss56@njit.edu'
    user.balance += 2022
    assert user.balance == 2022
    assert db.session.query(User).count() == 1

    with application.test_client(user=user) as client:
        response = client.get("/dashboard")
        assert response.status_code == 200
        # checking displaying email and balance on the dashboard
        assert b'hss56@njit.edu' in response.data
        assert b'Balance: 2022.0' in response.data
