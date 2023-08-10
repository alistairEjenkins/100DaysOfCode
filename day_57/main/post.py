class Post:

    def __init__(self, post_data):
        self.id = post_data['id']
        self.title = post_data['title']
        self.subtitle = post_data['subtitle']
        self.body = post_data['body']


    def __repr__(self):
        return f"{self.id} {self.title} {self.subtitle} {self.body}"