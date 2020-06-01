import os

class Config:
    '''
    General configuration parent class
    '''
    SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    EVERYTHING_SOURCE_BASE_URL = 'https://newsapi.org/v2/everything?sources={}&pageSize={}&apiKey={}'
    TOP_HEADLINES_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    EVERYTHING_BASE_URL = 'https://newsapi.org/v2/everything?sources=bbc-news,al-jazeera-english,cnn,independent,google-news,the-telegraph,mashable,the-lad-bible,buzzfeed,bloomberg,engadget,espn,fortune&sortBy=publishedAt&pageSize={}&apiKey={}'
    EVERYTHING_SEARCH_URL = 'https://newsapi.org/v2/everything?q={}&pageSize={}&apiKey={}'

     NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

    # title = "Home - News From Various News Sources"

    # return render_template('index.html')

class ProdConfig(Config):
    '''
    Production configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development configuration child class
    Args:
        Config: The parent configuration class with General configuration settings.
    '''
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
} 