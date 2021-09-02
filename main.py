from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from allform import BookForm, ContactForm
from datetime import datetime


# # Quiz:
# import requests
# from quizlet import Question, QuizBrain
# import html
#
# API_GENERAL = "https://opentdb.com/api.php?amount=10&type=boolean"
# API_ANIMAL = "https://opentdb.com/api.php?amount=10&category=27&type=boolean"


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BEfBA6O6dobnzWlSihBXox7C0sKR6b'
Bootstrap(app)

all_books = []

year = datetime.now().year

@app.route('/')
def home():
    return render_template("index.html")


@app.route('/game')

def game():
    with open('game.txt', 'r') as data:
        games = data.read().split('\n')
        g_list = [game.split(", ") for game in games]
        g_num = len(g_list)

    return render_template("game.html", games=g_list, num=g_num)

@app.route('/book')
def book():
    return render_template("book.html")


@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template("contact.html", form =form)

@app.route('/learning')
def learning():
    return render_template("learning.html")




@app.route("/donate")
def donate():
    form = BookForm()
    return render_template("donate.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
