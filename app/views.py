from flask import render_template
from app import app
from .requests import get_sources,get_headlines,get_articles 

# Views
@app.route('/')
def index():

    """
    View root page function that returns the index page and it's data
    """
    technology_source = get_sources('technology')
    business_source = get_sources('business')
    headlines_articles_news = get_headlines('headlines')
    # business_articles = get_articles('business')
    title = 'Home - Welcome to The best News Highlights Website Online'
    return render_template('index.html', title = title, technology = technology_source, business = business_source, headlines = headlines_articles_news)

@app.route('/sports/')
def sports():

    """
    View root page function that returns the index page and it's data
    """
    
    sports_source = get_sources('sports')
    entertainment_source = get_sources('entertainment')

    title = 'Home - Welcome to The best News Highlights Website Online'
    return render_template('sports.html', title = title, sports = sports_source, entertainment= entertainment_source)


@app.route('/articles/')
def articles():

    """
    View news page function that returns the news details page and it's data
    """
   
    business_articles = get_articles('business')
    # articles = get_articles(id)
    # print(articles)
    title = 'Home - Welcome to The best News Highlights Website Online'
    return render_template('articles.html', title = title, business =business_articles)

@app.route('/headlines/')
def headlines():

    """
    View news page function that returns the news details page and it's data
    """
   
    headlines_articles_news = get_headlines('headlines')
    # articles = get_articles(id)
    # print(articles)
    title = 'Home - Welcome to The best News Highlights Website Online'
    return render_template('headlines.html', title = title, headlines =headlines_articles_news)