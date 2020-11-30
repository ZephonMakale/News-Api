class Headlines:
    """
    Headlines class to define headlines objects
    """
    def __init__(self,name,author,title,description,url,urlToImage,publishedAt):
        self.name = name
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt