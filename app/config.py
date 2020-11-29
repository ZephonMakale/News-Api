class Config:
    """
    General configuration parent class
    """
    SOURCES_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&apiKey=c29e92dd8bf64550bf2cc7b2e50c79ca'
    
    

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