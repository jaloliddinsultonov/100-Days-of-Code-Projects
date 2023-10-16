from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def home():
    response = requests.get(url="https://api.npoint.io/eb6cd8a5d783f501ee7d")
    all_posts = response.json()
    return render_template("index.html", all_posts=all_posts)


@app.route("/about")
def get_about_me():
    return render_template("about.html")


@app.route("/contact")
def get_contact():
    return render_template("contact.html")


@app.route("/post/<num>")
def get_post(num):
    response = requests.get(url="https://api.npoint.io/eb6cd8a5d783f501ee7d")
    all_posts = response.json()
    num = int(num)
    return render_template("post.html", num=num, all_posts=all_posts)


if __name__ == "__main__":
    app.run()


