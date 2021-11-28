from flask import Blueprint
from flask import Flask, request, redirect, render_template
from .models import User, Listings
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods =["GET", "POST"])
def index():     
  return render_template("home.html")

@views.route("/listings", methods =["GET", "POST"])
def showListings():
  return render_template("/listings.html")

@views.route("/tabular_listings")
def listings():
    users = User.query.all()

    context = {
        "users": users
    }

    return render_template("/table.html", context=context)

@views.route("/create_listing", methods =["POST", "GET"])
def postListings():

    if request.method == "POST":
        email = request.form.get('input_email')
        phone = request.form.get('input_phone')
        fname = request.form.get('input_fname')
        lname = request.form.get('input_lname')
        title = request.form.get('input_title')
        location = request.form.get('input_location')
        description = request.form.get('input_desc')
        image = request.form.get('input_photo')

        poster = User(phone_number=phone, first_name=fname, last_name=lname, email=email)
        # listing = Listings(user=phone, title=title, description=description, location=location)

        user_exists = db.session.query(User.phone_number).filter_by(phone_number=poster.phone_number).first() is not None

        if not user_exists:
            db.session.add(poster)
            db.session.commit()

        users = User.query.all()

        context = {
            "users": users
        }
        return render_template("/table.html", context=context)

    if request.method == "GET":
        return render_template("/create_listing.html")



