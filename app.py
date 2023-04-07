from flask import Flask, render_template, url_for, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
from forms import Registration, Login, AdminSignup, AdminLogin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '12345asdfghqwertyugfdsswg123456'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/college'

db = SQLAlchemy(app)
socketio = SocketIO(app)

# database
class User(db.Model):
	u_id = db.Column(db.Integer, primary_key=True)
	u_name = db.Column(db.String(20), unique = True, nullable=False)
	u_email = db.Column(db.String(120), unique = True, nullable=False)
	u_picture = db.Column(db.String(20), nullable=False, default = 'user.jpg')
	u_password = db.Column(db.String(60), nullable=False)
	joined_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	u_bio = db.Column(db.Text, nullable=False)
	books = db.relationship('Books', backref= 'author', lazy='True')

	def __repr__(self):
		return f"User('{self.u_name}', '{self.u_id}', '{self.u_name}', '{self.u_picture}', '{self.u_password}', '{self.u_email}')"

class Books(db.Model):
	book_isbn = db.Column(db.Integer, primary_key = True)
	book_name = db.Column(db.String(20), unique = True, nullable=False)
	book_picture = db.Column(db.String(20), nullable= False, default = 'book.jpg')


	def __repr__(self):
		return f"User('{self.u_name}', '{self.u_id}', '{self.u_name}', '{self.u_picture}', '{self.u_password}', '{self.u_email}')"


@app.route('/')
@app.route('/home')
def home_page():
	return render_template('home.html', title='Home', link1='', link2='', link3='', link4='', toPage1='', toPage2='', toPage3='', toPage4='')

@app.route('/login')
@app.route('/sign-in')
def login():
	form = Login()
	return render_template('login.html', title='Login', form = form, link1='', link2='', link3='', link4='', toPage1='', toPage2='', toPage3='', toPage4='')

@app.route('/signup')
@app.route('/register')
def signup():
	form = Registration()
	return render_template('signup.html', title = 'Register', form=form, link1='', link2='', link3='', link4='', toPage1='', toPage2='', toPage3='', toPage4='')

@app.route('/user')
def user_profile():
	return render_template('user.html', title='Profile', link1='', link2='', link3='', link4='', toPage1='', toPage2='', toPage3='', toPage4='')

@app.route('/recommend')
def recommend():
	return render_template('recommend.html', title='Recommend', link1='', link2='', link3='', link4='', toPage1='', toPage2='', toPage3='', toPage4='')

@app.route('/home-room')
def room_chat():
	return render_template('room_home.html', title='Room Home', link1='', link2='', link3='', link4='', toPage1='', toPage2='', toPage3='', toPage4='')

@app.route('/admin-login')
def adminLogin():
	form=AdminLogin()
	return render_template('admin_login.html', title='Admin Login', link1='', link2='', link3='', link4='', toPage1='', toPage2='', toPage3='', toPage4='')

@app.route('/admin-signup')
def adminSignup():
	form=AdminSignup()
	return render_template('admin_signup.html', title='Admin Signup', link1='', link2='', link3='', link4='', toPage1='', toPage2='', toPage3='', toPage4='')

if __name__ == '__main__':
    app.run(debug=True)
    
'''
from flaskblog import db

db.create_all()

from flaskblog import User, Books

user1 = User(username = 'Cherry' etc...)
db.session.add(user1)

db.session.commit()

User.query.all()
User.query.first()
User.query.filter_by(uname = 'c')
User.quer.get(1)
'''
