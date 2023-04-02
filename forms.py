from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)])
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('password', validators = [DataRequired()])
	confirm_password = PasswordField('confirm password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign up')

class Login(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	password = PasswordField('password', validators = [DataRequired()])
	remember = BooleanField('Remember Me ')
	submit = SubmitField('Login')

class AddBook(FlaskForm):
	book_title = StringField('Book Title', validators = [DataRequired()])
	book_author = StringField('Book Author', validators = [DataRequired()])
	book_picture = StringField('Book Picture', validators = [DataRequired()])
	submit = SubmitField('Add to Database')