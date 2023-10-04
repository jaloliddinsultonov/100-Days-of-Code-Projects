from flask import Flask, render_template
from post import get_dictionary


app = Flask(__name__)


@app.route('/')
def home():
    blogs = get_dictionary()
    return render_template("index.html", blogs=blogs)


@app.route('/post/<num>')
def get_blog(num):
    posts = get_dictionary()
    num = int(num) - 1
    return render_template("post.html", posts=posts, num=num)


if __name__ == "__main__":
    app.run(debug=True)
