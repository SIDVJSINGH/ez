import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'you-will-never-guess')
    MONGODB_URL = os.environ.get('MONGODB_URL', 'mongodb://localhost:27017/')
