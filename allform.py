from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from wtforms import StringField, SubmitField, IntegerField, TextAreaField, PasswordField
from wtforms.validators import InputRequired, Email, NumberRange, Length, DataRequired

class BookForm(FlaskForm):
    book_name = StringField('Book Name', validators=[InputRequired()])
    book_author = StringField('Book Author', validators=[InputRequired()])
    rating = IntegerField('Rating', validators=[NumberRange(min=1, max=10), InputRequired()])
    book_file = FileField('Upload Book', validators=[FileRequired()])
    submit = SubmitField('Add')
    
class ContactForm(FlaskForm):
    full_name = StringField('Full Name', validators=[InputRequired()]) 
    email = StringField('Email', validators=[InputRequired(), Email()])
    location = StringField('State, Country', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])
    submit = SubmitField('Send')

class LogInForm(FlaskForm):
    username = StringField('username', validators=[Length(min=5, max=120)])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Log In')
    
