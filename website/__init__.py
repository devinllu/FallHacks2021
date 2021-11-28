from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path

db = SQLAlchemy()
DB_NAME = "database.db"

from .views import views
from .models import User, Listings, Images

def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    app.register_blueprint(views, url_prefix='/')
    create_database(app)
    create_fake_data(app)
    test_db(app)
    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

def test_db(app):
    with app.app_context():
        users = User.query.all()

        print(len(users))

def create_fake_data(app):
    a1 = User(phone_number="6041902090", first_name="Devin", last_name="Lu", email="ludevinl@sfu.ca")
    a2 = User(phone_number="7781092903", first_name="Joe", last_name="LeTran", email="joe@sfu.ca")
    a3 = User(phone_number="6041010923", first_name="John", last_name="Ko", email="john@sfu.ca")
    a4 = User(phone_number="7781234567", first_name="Amelia", last_name="Abance", email="amelia@sfu.ca")
    a5 = User(phone_number="6041234567", first_name="Curtis", last_name="Reyes", email="curtis@sfu.ca")
    a6 = User(phone_number="7782134123", first_name="Jake", last_name="Lahsinia", email="jake@sfu.ca")
    a7 = User(phone_number="6040192834", first_name="Jonathan", last_name="Lasagna", email="jonathan@sfu.ca")
    a8 = User(phone_number="7781019212", first_name="Don", last_name="Doe", email="don@sfu.ca")
    a9 = User(phone_number="7780987654", first_name="Amos", last_name="Love", email="amos@sfu.ca")

    lst = [a1, a2, a3, a4, a5, a6, a7, a8, a9]

    for entries in lst:
        with app.app_context():
            exists = db.session.query(User.phone_number).filter_by(phone_number=entries.phone_number).first() is not None
            if not exists:
                db.session.add(entries)
                db.session.commit()
    