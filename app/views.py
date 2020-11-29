from flask import render_template
from app import app
from .requests import get_sources

# Views
@app.route('/')
def index():

    """
    View root page function that returns the index page and it's data
    """
    political_articles = get_sources('political')
    business_articles = get_sources('business')
    sports_articles = get_sources('sports')
    print(political_articles)
    title = 'Home - Welcome to The best News Highlights Website Online'
    return render_template('index.html', title = title, political = political_articles, business = business_articles, sports= sports_articles)


@app.route('/articles/<int:articles_id>')
def articles(articles_id):

    """
    View news page function that returns the news details page and it's data
    """
    return render_template('articles.html', id = articles_id)