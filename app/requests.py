import json
import urllib.request
from datetime import datetime

from .models import Articles, Sources

apiKey = None
sources_url = None
articles_url = None
topheadlines_url = None
everything_url = None
everything_search_url = None


def configure_request(app):
    global apiKey, sources_url, articles_url, topheadlines_url
    apiKey = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_BASE_URL']
    articles_url = app.config['ARTICLE_SOURCE_BASE_URL']
    topheadlines_url = app.config['TOP_HEADLINES_BASE_URL']


def get_sources(category):
    '''
    Function that gets the json response to out url request
    '''
    get_sources_url = sources_url.format(category, apiKey)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results = process_results(get_sources_response['sources'])

            return sources_results


def process_results(sources_list):
    '''
    Function that process our json results
    '''
    sources_results = []

    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        country = source.get('country')

        if url:
            source_object = Sources(
                id, name, description, url, category, country)
            sources_results.append(source_object)

    return sources_results


def get_articles(source_id, limit, article):
    '''
    Function that gets articles based on the source id
    '''
    get_article_location_url = articles_url.format(source_id, article, apiKey)

    with urllib.request.urlopen(get_article_location_url) as url:
        articles_location_data = url.read()
        articles_location_response = json.loads(articles_location_data)

        articles_location_results = None

        if articles_location_response['articles']:
            articles_location_results = process_articles(
                articles_location_response['articles'])

            return articles_location_results


def process_articles(my_articles):
    '''
    Function that process the json results for the articles
    '''
    article_location_list = []

    for article in my_articles:
        author = article.get('author')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        date_published = article.get('publishedAt')

        publishedAt = datetime(year=int(date_published[0:4]), month=int(date_published[5:7]), day=int(
            date_published[8:10]), hour=int(date_published[11:13]), minute=int(date_published[14:16]))

        if urlToImage:
            article_source_object = Articles(
                author, title, description, url, urlToImage, publishedAt)
            article_location_list.append(article_source_object)

    return article_location_list


def topheadlines(category):
    '''
    Function that gets articles based on the source id
    '''
    get_topheadlines_url = topheadlines_url.format(apiKey)

    with urllib.request.urlopen(get_topheadlines_url) as url:
        topheadlines_data = url.read()
        topheadlines_response = json.loads(topheadlines_data)

        topheadlines_results = None

        if topheadlines_response['articles']:
            topheadlines_results = process_articles(
                topheadlines_response['articles'])

    return topheadlines_results
