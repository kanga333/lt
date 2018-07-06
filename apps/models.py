from apps.database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)

    def __repr__(self):
        return f"<User> id={self.id}, name={self.name}, email={self.email}"


class Lt(db.Model):
    __tablename__ = 'lt'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Text)


class Talk(db.Model):
    __tablename__ = 'talk'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    lt_id = db.Column(db.Integer)
    title = db.Column(db.Text)
    presentation_time = db.Column(db.Integer)


def init():
    db.create_all()
