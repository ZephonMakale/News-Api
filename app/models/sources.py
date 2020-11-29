class Sources:
    '''
    News class to define News Objects
    '''
    def __init__(self,id,name,description,url,category,language,country):
        self.id = id
        self.name = name
        self.description = description
        self.url = url
        self.category = category
        self.language = language
        self.country = country
    # def __init__(self,source,articles,id,author,title,description,url,urlToImage,publishedAt,content):
    #     self.source =source
    #     self.articles = articles
    #     self.author = 'https://image.tmdb.org/t/p/w500/'+ author
    #     self.title = title
    #     self.description = description
    #     self.url = url
    #     self.urlToImage = urlToImage
    #     self.publishedAt = publishedAt
    #     self.content = content