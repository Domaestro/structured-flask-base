class config(object):
    # Определяет, включен ли режим отладки
    # В случае если включен, flask будет показывать
    # подробную отладочную информацию. Если выключен -
    # - 500 ошибку без какой либо дополнительной информации.
    DEBUG = True

    # Включение защиты против "Cross-site Request Forgery (CSRF)"
    CSRF_ENABLED = True

    # Случайный ключ, которые будет исползоваться для подписи
    # данных, например cookies.
    SECRET_KEY = '11#@*y492feh'

    # URI используемая для подключения к базе данных
    SQLALCHEMY_DATABASE_URI = "sqlite:///mydb.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    test = "fefe"