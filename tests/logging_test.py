import os
from app import config

""" Tests to check log files exist """


def test_log_dir_creation(client):
    logdir = config.Config.LOG_DIR
    assert os.path.exists(logdir) is True


def test_debug_log_file_creation(client):
    logdir = config.Config.LOG_DIR
    logfile = os.path.join(logdir, './handler.log')
    assert os.path.exists(logfile) is True


def test_request_log_file_creation(client):
    logdir = config.Config.LOG_DIR
    logfile = os.path.join(logdir, './request.log')
    assert os.path.exists(logfile) is True


def test_werkzeug_log_file_creation(client):
    logdir = config.Config.LOG_DIR
    logfile = os.path.join(logdir, './werkzeug.log')
    assert os.path.exists(logfile) is True


def test_errors_log_file_creation(client):
    logdir = config.Config.LOG_DIR
    logfile = os.path.join(logdir, './errors.log')
    assert os.path.exists(logfile) is True


def test_myapp_log_file_creation(client):
    logdir = config.Config.LOG_DIR
    logfile = os.path.join(logdir, './myapp.log')
    assert os.path.exists(logfile) is True


def test_sqlalchemy_log_file_creation(client):
    logdir = config.Config.LOG_DIR
    logfile = os.path.join(logdir, './sqlalchemy.log')
    assert os.path.exists(logfile) is True


def test_uploads_log_file_creation(client):
    logdir = config.Config.LOG_DIR
    logfile = os.path.join(logdir, './uploads.log')
    assert os.path.exists(logfile) is True


def test_activity_log_file_creation(client):
    logdir = config.Config.LOG_DIR
    logfile = os.path.join(logdir, './user_activity.log')
    assert os.path.exists(logfile) is True
