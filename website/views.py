from flask import Blueprint
from flask import Flask, request, redirect, render_template

views = Blueprint('views', __name__)

@views.route('/', methods =["GET", "POST"])
def index():     
  return render_template("base.html")