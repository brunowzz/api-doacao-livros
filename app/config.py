import os

class Config:
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
    DATABASE = os.path.join('instance', 'database.db')