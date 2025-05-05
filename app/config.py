import os

class Config:
    DEBUG = False
    TESTING = False
    DB_NAME = "todos.db"
    SECRET_KEY = os.environ.get('SECRET_KEY', 'supersecret')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DB_NAME = "/var/data/todos.db"
