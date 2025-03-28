import os

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'
    DATABASE = os.path.join('instance', 'database.db')