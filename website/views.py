from flask import Blueprint
from flask import Flask, request, redirect, render_template
from .models import User, Listings
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods =["GET", "POST"])
def index():     
  return render_template("base.html")

@views.route("/listings", methods =["GET", "POST"])
def showListings():
  return render_template("/listings.html")

@views.route("/create_listing", methods =["POST", "GET"])
def postListings():

    if request.method == "POST":
        email = request.form['input_email']
        phone = request.form['input_phone']
        fname = request.form['input_fname']
        lname = request.form['input_lname']
        title = request.form['input_title']
        location = request.form['input_location']
        description = request.form['input_desc']
        image = request.form['input_photo']

        poster = User(phone_number=phone, first_name=fname, last_name=lname, email=email)
        listing = Listings(phone, title, description, location)

        user_exists = db.session.query(User.phone_number).filter_by(phone_number=poster.phone_number).first() is not None

        if not user_exists:
            db.session.add(poster)
            db.session.commit()

    if request.method == "GET":
        return render_template("/create_listing.html")



