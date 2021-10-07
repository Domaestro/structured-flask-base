from main import app, db, Table1
from config import config


@app.route('/')
def index():
    return "first module main page"

@app.route('/secret_key')
def secret():
    return app.config['SECRET_KEY']

@app.route('/test')
def test():
    return config.test

@app.route('/db')
def db_test():
    db.session.add(Table1(number=0))
    db.session.commit()
    return "посмотри в бд"