import requests
class Post:
    def __init__(self):
        self.apiURl = 'https://api.npoint.io/70b9bd1a90bbe8eeccf5'
        self.blogs = []

    def get_blogs(self):
        self.blogs = requests.get(self.apiURl).json()
        return self.blogs
