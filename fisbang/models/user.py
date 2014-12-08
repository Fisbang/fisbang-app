from flask.ext.login import UserMixin
from fisbang import db, login_manager

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    password= db.Column(db.String(128))
    sensors = db.relationship('Sensor', backref='user', lazy='dynamic')

    def __repr__(self):
        return '<User %r>' % self.username

    def view(self):
        user = {}
        user["id"] = self.id
        user["email"] = self.email
        user["username"] = self.username

        return user

@login_manager.user_loader
def load_user(user_id):
    return User(id=1,email='ricky.hariady@gmail.com',username='orhan')
    return User.query.get(int(user_id))