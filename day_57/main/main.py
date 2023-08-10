from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

def read_data():
    response = requests.get(' https://api.npoint.io/c790b4d5cab58020d391')
    response.raise_for_status()
    all_posts = response.json()
    return [Post(post_data) for post_data in all_posts]

@app.route('/')
def home():
    return render_template("index.html", all_posts= all_posts)

@app.route('/post/<string:blog_id>')
def blog(blog_id):

    post = all_posts[int(blog_id) -1]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    all_posts = read_data()
    app.run(debug=True)

