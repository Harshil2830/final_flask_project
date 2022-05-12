import os
import click
from flask.cli import with_appcontext
from app.db import db


@click.command(name='create-db')
@with_appcontext
def create_database():
    # get root directory of project
    root = os.path.dirname(os.path.abspath(__file__))
    # set db directory
    db_dir = os.path.join(root, '../../database')
    # make a directory if it doesn't exist
    if not os.path.exists(db_dir):
        os.mkdir(db_dir)
    db.create_all()

