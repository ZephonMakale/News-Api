class Config:
    """
    General configuration parent class
    """
    SOURCES_API_BASE_URL ='https://newsapi.org/v2/sources?category={}&apiKey={}'
    ARTICLES_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&apiKey=c4c90179abd44016b3575b8a4b9f2a61&limit=5'
    HEADLINES_API_BASE_URL ='https://newsapi.org/v2/top-headlines?country=us&apiKey=c4c90179abd44016b3575b8a4b9f2a61&limit=5'
    
    

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