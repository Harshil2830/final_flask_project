import os
from click.testing import CliRunner
from app import create_database

runner = CliRunner()


def test_create_database():
    response = runner.invoke(create_database)
    assert response.exit_code == 0
    root = os.path.dirname(os.path.abspath(__file__))
    db_dir = os.path.join(root, '../database')
    assert os.path.exists(db_dir) is True
