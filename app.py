from flask import Flask, render_template, url_for, request, session, redirect
from flask_socketio import join_room, leave_room, send, SocketIO
from forms import Registration, Login
from flask_sqlalchemy import SQLAlchemy

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
	u_picture = db.Column(db.String(20), nullable=False, default = 'default.jpg')
	u_password = db.Column(db.String(60), nullable=False)

	def __repr__(self):
		return f"User('{self.u_name}', '{self.u_id}', '{self.u_name}', '{self.u_picture}', '{self.u_password}', '{self.u_email}')"

@app.route('/')
@app.route('/home')
def home_page():
	return render_template('home.html', title='Home')

@app.route('/login')
@app.route('/sign-in')
def login():
	form = Login()
	return render_template('login.html', title='Login', form = form)

@app.route('/signup')
@app.route('/register')
def signup():
	form = Registration()
	return render_template('signup.html', title = 'Register', form=form)

@app.route('/user')
def user_profile():
	return render_template('user.html', title='Profile')

@app.route('/recommend')
def recommend():
	return render_template('recommend.html', title='Profile')

@app.route('/home-room')
def room_chat():
	return render_template('room_home.html', title='Room Home')

@app.route('/admin-login')
def adminLogin():
	return render_template('admin_login.html', title='Admin')

if __name__ == '__main__':
    app.run(debug=True)