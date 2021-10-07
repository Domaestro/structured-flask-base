from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    abort,
    redirect,
    url_for,
    current_app,
)

from config import config
from main import db, Table1

module = Blueprint('entity', __name__, url_prefix ='/entity')


@module.route('/')
def index():
    return "first module main page"

@module.route('/secret_key')
def secret():
    return config.SECRET_KEY

@module.route('/test')
def test():
    return config.test

@module.route('/db')
def db_test():
    db.session.add(Table1(number=0))
    db.session.commit()
    return "посмотри в бд"
