from flask import render_template
from init import flask_app
from .forms import LoginForm

@flask_app.route('/')
@flask_app.route('/index')
@flask_app.route('home')
def index():
    return render_template("index.html",)