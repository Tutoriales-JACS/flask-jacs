from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


def create_app(envirom):
    app = Flask(__name__)
    app.config.from_object(envirom)
    db.init_app(app)
    ma.init_app(app)


    from .routes import api_bp
    app.register_blueprint(api_bp)

   
    with app.app_context():
        db.create_all()
    
    return app