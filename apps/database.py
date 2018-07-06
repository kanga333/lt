from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def init_db(app):
    app.config.from_object('apps.config.Config')
    db.init_app(app)
    Migrate(app, db)
