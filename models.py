from app import db
from datetime import datetime

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

