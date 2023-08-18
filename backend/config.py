import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

class DevConfig():
    DEBUG=True
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_RECORD_QUERIES=True