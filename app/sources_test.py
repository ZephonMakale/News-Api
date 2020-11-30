import unittest
from models import sources,articles,headlines

Sources = sources.Sources
Articles = articles.Articles
Headlines = headlines.Headlines

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Sources(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_articles = Articles(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_articles,Articles))

class HeadlinesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''
    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_headlines = Headlines(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)
    def test_instance(self):
        self.assertTrue(isinstance(self.new_headlines,Headlines))

if __name__ == '__main__':
    unittest.main()

