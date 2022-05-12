import os
from app import config


def test_log_dir_creation(client):
    logdir = config.Config.LOG_DIR
    assert os.path.exists(logdir) is True
