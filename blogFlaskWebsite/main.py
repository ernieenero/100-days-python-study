from flask import Flask, render_template
from post import Post
from datetime import datetime
app = Flask(__name__)

# get the class post to get the blog post from api
blog_post = Post()
blogs = blog_post.get_blogs()

currentyear = datetime.now().year

@app.route('/')
def home():
    return render_template("index.html", blogs=blogs, currentyear=currentyear)

@app.route('/post/<int:blogid>')
def blog_post(blogid):
    blog_data = blogs[blogid-1]
    return render_template('post.html', data=blog_data, currentyear=currentyear)

if __name__ == "__main__":
    app.run(debug=True)
