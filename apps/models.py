from apps.database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    email = db.Column(db.Text)

    def __repr__(self):
        return f"<User> id={self.id}, name={self.name}, email={self.email}"


def init():
    db.create_all()
