from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_sources,get_headlines,get_articles,search_sources
from ..models import Headlines, Sources, Articles

# Views
@main.route('/')
def index():

    """
    View root page function that returns the index page and it's data
    """
    technology_source = get_sources('technology')
    business_source = get_sources('business')
    headlines_articles_news = get_headlines('headlines')
    # business_articles = get_articles('business')
    title = 'Home - Welcome to The best News Highlights Website Online'
    search_sources = request.args.get('sources_')

    if search_sources:
        return redirect(url_for('search',category=search_sources))
    else:
        return render_template('index.html', title = title, technology = technology_source, business = business_source, headlines = headlines_articles_news)

@main.route('/sports/')
def sports():

    """
    View root page function that returns the index page and it's data
    """
    
    sports_source = get_sources('sports')
    entertainment_source = get_sources('entertainment')

    title = 'Home - Welcome to The best News Highlights Website Online'
    return render_template('sports.html', title = title, sports = sports_source, entertainment= entertainment_source)


@main.route('/articles/')
def articles():

    """
    View news page function that returns the news details page and it's data
    """
   
    business_articles = get_articles('business')
    # articles = get_articles(id)
    # print(articles)
    title = 'Home - Welcome to The best News Highlights Website Online'
    return render_template('articles.html', title = title, business =business_articles)

@main.route('/headlines/')
def headlines():

    """
    View news page function that returns the news details page and it's data
    """
   
    headlines_articles_news = get_headlines('headlines')
    # articles = get_articles(id)
    # print(articles)
    title = 'Home - Welcome to The best News Highlights Website Online'
    return render_template('headlines.html', title = title, headlines =headlines_articles_news)

@main.route('/search/<sources_name>')
def sourcesSearch(sources_name):
    '''
    View function to display the search results
    '''
    search_sources_name = sources_name.split(" ")
    search_name_format = "+".join(search_sources_name)
    searched_sources = search_sources(search_name_format)
    # title = f'search results for {sources_name}'
    return render_template('search.html',sources = searched_sources)