class Config:
    '''Clase de configuracion de Flask'''
    SECRET_KEY = 'Ideas'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../../ideas.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False