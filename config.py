import os 

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # setting up the configuration for the application. pull from environment variables using os.environ.get()
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db') # if not database set up, create sqlite db in main directory
    SQLALCHEMY_TRACK_MODIFICATIONS = False