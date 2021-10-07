from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config


# Инициализация и добавление конфигурации приложения
app = Flask(__name__)
app.config.from_object(config)


# Подключение базы данных и ее таблиц
db = SQLAlchemy(app)

class Table1(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    def __str__(self):
        return self.name


# Импорт представлений
from routes import *    


# Регистрация блюпринтов
from firstmodule.controllers import module
app.register_blueprint(module, url_prefix='/1')


# Запуск приложения
if __name__ == '__main__':
    app.run()