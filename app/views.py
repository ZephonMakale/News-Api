from flask import render_template
from app import app
from .requests import get_sources,get_headlines,get_articles 

# Views
@app.route('/')
def index():

    """
    View root page function that returns the index page and it's data
    """
    political_source = get_sources('political')
    headlines_articles_news = get_headlines('headlines')
    business_articles = get_articles('business')
    title = 'Home - Welcome to The best News Highlights Website Online'
    return render_template('index.html', title = title, political = political_source, headlines = headlines_articles_news, business = business_articles)


# @app.route('/articles/<int:articles_id>')
# def articles(articles_id):

#     """
#     View news page function that returns the news details page and it's data
#     """
   
#     business_articles = get_articles('business')
#     print(business_articles)
#     return render_template('articles.html', id = articles_id)