from sqlalchemy.sql.expression import desc
from . import db
from sqlalchemy.sql import func

class User(db.Model):
	phone_number = db.Column(db.String(10), primary_key=True)
	first_name = db.Column(db.String(26), nullable=False)
	last_name = db.Column(db.String(26), nullable=False)
	email = db.Column(db.String(320), nullable=False)

	def __init__(self, phone_number, first_name, last_name, email):
		self.phone_number = phone_number
		self.first_name = first_name
		self.last_name = last_name
		self.email = email


class Listings(db.Model):
	user = db.Column(db.String(10), db.ForeignKey("user.phone_number"), primary_key=True)
	listing_id = db.Column(db.String(10), primary_key=True)
	title = db.Column(db.String(128), nullable=False)
	description = db.Column(db.String(512), nullable=False)
	location = db.Column(db.String(1024), nullable=False)

	def __init__(self, user, title, description, location):
		self.user = user
		# self.listing_id = listing_id
		self.title = title
		self.description = description
		self.location = location


class Images(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	img_1 = db.Column(db.String(255))
	img_2 = db.Column(db.String(255))
	img_3 = db.Column(db.String(255))

	def __init__(self, id, img_1, img_2, img_3):
		self.id = id
		self.img_1 = img_1
		self.img_2 = img_2
		self.img_3 = img_3