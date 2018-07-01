from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def init_db(app):
    app.config.from_object('apps.config.Config')
    db.init_app(app)
