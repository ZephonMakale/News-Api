import urllib.request,json
from .models import Sources, Headlines, Articles

sources_url = None
api_key = None
base_url = None
base_url2 = None
base_url3 = None
base_url3 = None

def configure_request(app):
    global api_key,base_url,base_url3,base_url2
    api_key = app.config['SOURCES_API_KEY']
    base_url = app.config['SOURCES_API_BASE_URL']
    base_url2 = app.config['ARTICLES_API_BASE_URL']
    base_url3 = app.config['HEADLINES_API_BASE_URL']
    # sources_url = app.config['SOURCES_API_BASE_URL']

# Sources = sources.Sources
# Articles = articles.Articles
# Headlines = headlines.Headlines

def get_sources(category):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(category,api_key)
    # get_sources_url = 'https://newsapi.org/v2/sources?category=entertainment&apiKey=aec6f4d84dae4ec8a599e4bacbaed3ca'

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)
        print(get_sources_response)
        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results = process_results(sources_results_list)
    
    return sources_results
    

def process_results(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects

    Args:
        movie_list: A list of dictionaries that contain movie details

    Returns :
        movie_results: A list of movie objects
    '''
    sources_results = []
    for sources_item in sources_list:
        id = sources_item.get('id')
        name = sources_item.get('name')
        description = sources_item.get('description')
        url = sources_item.get('url')
        category = sources_item.get('category')
        language = sources_item.get('language')
        country = sources_item.get('country')

        sources_object = Sources(id,name,description,url,category,language,country)
        sources_results.append(sources_object)

    return sources_results




def get_articles(category):
    get_articles_url = base_url2.format(category,api_key)

    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)

        articles_results = None

        if get_articles_response['articles']:
            articles_results_list = get_articles_response['articles']
            articles_results = process_articles(articles_results_list)
    
    return articles_results

def process_articles(articles_list):
    articles_results = []
    for articles_item in articles_list:
        author = articles_item.get('author')
        title = articles_item.get('title')
        description = articles_item.get('description')
        url = articles_item.get('url')
        urlToImage = articles_item.get('urlToImage')
        publishedAt = articles_item.get('publishedAt')
        content = articles_item.get('content')

        articles_object = Articles(author,title,description,url,urlToImage,publishedAt,content)
        articles_results.append(articles_object)

    return articles_results





def get_headlines(category):
    get_headlines_url = base_url3.format(category,api_key)

    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response['articles']:
            headlines_results_list = get_headlines_response['articles']
            headlines_results = process_headlines(headlines_results_list)
    
    return headlines_results

def process_headlines(headlines_list):
    headlines_results = []
    for headlines_item in headlines_list:
        source = headlines_item.get('source')
        author = headlines_item.get('author')
        title = headlines_item.get('title')
        description = headlines_item.get('description')
        url = headlines_item.get('url')
        urlToImage = headlines_item.get('urlToImage')
        publishedAt = headlines_item.get('publishedAt')

        headlines_object = Headlines(source,author,title,description,url,urlToImage,publishedAt)
        headlines_results.append(headlines_object)

    return headlines_results

def search_sources(category):
    search_url = base_url.format(category,api_key)

    with urllib.request.urlopen(search_url) as url:
        search_data = url.read()
        search_response = json.loads(search_data)

        search_results = None

        if search_response['sources']:
            all_search_results = search_response['sources']
            search_outcome = process_results(all_search_results)
    return search_outcome