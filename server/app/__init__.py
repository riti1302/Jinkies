from flask import Flask

app = None


def create_app():
    global app
    app = Flask(__name__)
    from app import views
    return app
