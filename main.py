from flask import Flask, render_template,redirect, url_for
from flask_bootstrap import Bootstrap
from allform import BookForm, ContactForm
from datetime import datetime
import os
from werkzeug import secure_filename
import sqlite3


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

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL, file varchar(250) NOT NULL)")
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
    return render_template("book.html", books = all_books)


@app.route('/contact')
def contact():
    form = ContactForm()
    return render_template("contact.html", form =form)

@app.route('/learning')
def learning():
    return render_template("learning.html")




@app.route("/donate", methods=['GET', 'POST'])
def donate():
    form = BookForm()
    if form.validate_on_submit():
        book_name = form.book_name.data
        author = form.book_author.data
        rating = form.rating.data
        file = form.book_file.data
        all_books.append([book_name, author, rating, file])
        print(all_books)
        return redirect(url_for('book'))

    return render_template("donate.html", form=form)



if __name__ == "__main__":
    app.run(debug=True)
