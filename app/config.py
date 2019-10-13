import os

class Config:

    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}



# class DevConfig(Config):
#     '''
#     Development  configuration child class

#     Args:
#         Config: The parent configuration class with General configuration settings
#     '''

#     DEBUG = True
#     MOVIE_API_KEY = '<6129bce4662969a52564c4517d4911de>'
#     class Config:
#       '''
#       General configuration parent class
#       '''
#     MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'