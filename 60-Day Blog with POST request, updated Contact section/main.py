from flask import Flask, render_template, request
import requests
import smtplib

EMAIL = "reenoxgooglov@gmail.com"
PASSWORD = "mzbwcvsdbsyhahms"

posts = requests.get("https://api.npoint.io/eb6cd8a5d783f501ee7d").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/contact", methods=["GET", "POST"])
def receive_data():
    if request.method == "POST":
        # 1st way
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", message="Successfully sent your message")
    else:
        return render_template("contact.html")
    # 2nd way
    # data = request.form
    # print(data['name'])
    # print(data['email'])
    # print(data['phone'])
    # print(data['message'])
    # return f"Sucessfully sent your message"


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(EMAIL, "aladdinjakubowski@gmail.com", email_message)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
