import os

class Config:
    """
    General configuration parent class
    """
    SOURCES_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLES_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey=aec6f4d84dae4ec8a599e4bacbaed3ca&limit=5'
    HEADLINES_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey=aec6f4d84dae4ec8a599e4bacbaed3ca&limit=5'
    SECRET_KEY =os.environ.get('SECRET_KEY')
    SOURCES_API_KEY = os.environ.get('SOURCES_API_KEY')
    
    

class ProdConfig(Config):
    """
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    """
    pass

class DevConfig(Config):
    """
    Development configuration child class

    Args:
         Config: The parent configuration class with General configuration settings
    """

    DEBUG = True
config_options = {
    'development':DevConfig,
    'production':ProdConfig
}