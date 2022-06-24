import os

from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY="mikey",
        DATABASE_HOST=os.environ.get("Flask_DATABASE_HOST"),
        DATABASE_PASSWORD=os.environ.get("Flask_DATABASE_PASSWORD"),
        DATABASE_USER=os.environ.get("Flask_DATABASE_USER"),
        DATABASE=os.environ.get("Flask_DATABASE"),
    )

    @app.route('/hola')
    def hola():
        return 'Chanchito Feliz'
    
    return app
