from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def home():
    return f"<h1 style='text-align:center'>Guess a number between 0 and 9</h2>" \
           f"<center><img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' " \
           f"style='text-align:center'></center>"


random_number = random.randint(0, 9)


def lower():
    return f"<h1 style='text-align:center; color:red'>Too low, try again!</h2>" \
           f"<center><img src='https://media.giphy.com/media/qBVEww0YjwWyI/giphy.gif'></center>"


def higher():
    return f"<h1 style='text-align:center; color:red'>Too high, try again!</h2>" \
           f"<center><img src='https://media.giphy.com/media/AHMHuF12pW4b6/giphy.gif'></center>"


def correct():
    return f"<h1 style='text-align:center; color:green'>You found me!</h2>" \
           f"<center><img src='https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif'></center>"


@app.route("/<number>")
def page(number):
    number = int(number)
    if number > random_number:
        return higher()
    elif number < random_number:
        return lower()
    else:
        return correct()


if __name__ == "__main__":
    app.run(debug=True)