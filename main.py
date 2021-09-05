from flask import Flask
from flask import render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from allform import BookForm, ContactForm, LogInForm
from datetime import datetime
import os
from werkzeug.utils import secure_filename

# # Quiz:
# import requests
# from quizlet import Question, QuizBrain
# import html
#
# API_GENERAL = "https://opentdb.com/api.php?amount=10&type=boolean"
# API_ANIMAL = "https://opentdb.com/api.php?amount=10&category=27&type=boolean"


app = Flask(__name__)
# Secret Key
app.config['SECRET_KEY'] = '8BEfBA6O6dobnzWlSihBXox7C0sKR6b'
# Add Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books_up.db'
#Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Initialize Database
db = SQLAlchemy(app)
Bootstrap(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    file_path = db.Column(db.String(1550), nullable=False)


db.create_all()
db.session.commit()

uploads_dir = os.path.join(app.static_folder, 'book_uploads')
os.makedirs(uploads_dir, exist_ok=True)




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


@app.route('/book', methods=(["POST", "GET"]))
def book():
    form = LogInForm()
    all_books = db.session.query(Book).all()
    msg = "Admin Must Login To Edit Book Library"
    is_authenticated = False
    if request.method == 'POST' and form.validate_on_submit():
        if form.username.data == "admin" and form.password.data == "12345678":
            is_authenticated = True
        else:
            msg = "Wrong password. Please try again."
    return render_template("book.html", books=all_books, msg=msg, form=form, is_authenticated = is_authenticated)


@app.route('/contact', methods=(["POST", "GET"]))
def contact():
    sent = False
    form = ContactForm()
    if request.method=="POST":
        sent = True
        return render_template("contact.html", sent = sent)
    return render_template("contact.html", sent = sent)


@app.route('/learning')
def learning():
    return render_template("learning.html")


@app.route("/donate", methods=['GET', 'POST'])
def donate():
    form = BookForm()
    if form.validate_on_submit():
        file = form.book_file.data
        file_name = (file.filename).replace("_","").replace(" ", "")
        file.save(os.path.join(uploads_dir, secure_filename(file_name)))
        file_link = "/static/book_uploads/"+ file_name
        print(file_link)
        new_book = Book(
        title = form.book_name.data,
        author = form.book_author.data,
        rating = form.rating.data,
        file_path = file_link )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('book'))

    return render_template("donate.html", form=form)


@app.route('/delete')
def delete():
    book_id = request.args.get('id')

    # DELETE A RECORD BY ID
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('book'))



if __name__ == "__main__":
    app.run(debug=True)
