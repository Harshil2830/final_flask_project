import logging

from app import db
from app.db.models import User, Transaction


def test_adding_user(application):
    log = logging.getLogger("myApp")
    with application.app_context():
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
        # showing how to add a record
        # create a record
        user = User('hss56@njit.edu', 'testtest', 0)
        # add it to get ready to be committed
        db.session.add(user)
        db.session.commit()
        # assert that we now have a new user
        assert db.session.query(User).count() == 1
        # finding one user record by email
        user = User.query.filter_by(email='hss56@njit.edu').first()
        log.info(user)
        # asserting that the user retrieved is correct
        assert user.email == 'hss56@njit.edu'
        # this is how you get a related record ready for insert
        user.transactions = [Transaction(2022, "Credit"), Transaction(22, "Debit")]
        # saving the transaction
        db.session.commit()
        assert db.session.query(Transaction).count() == 2
        transaction1 = Transaction.query.filter_by(amount=2022).first()
        assert transaction1.amount == 2022

        transaction2 = Transaction.query.filter_by(amount=22).first()
        assert transaction2.amount == 22
        transaction2.amount = 2020
        assert transaction2.amount == 2020
        # checking cascade delete
        db.session.delete(user)
        assert db.session.query(User).count() == 0
        assert db.session.query(Transaction).count() == 0
