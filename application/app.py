from flask import Flask
from application.bp.homepage.homepage import homepage

def init_app():
    app = Flask(__name__)
    app.register_blueprint(homepage)
    return app
