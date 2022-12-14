from app import db, login_manager
import os
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class BaseModel():
    """
    This Class describe SQLAlchemy DB model with Basic CRUD functionality

    atribs:
        - id: primery key
        - create
        - update
        - delete
        - save
        - read
    """

    def create(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def update_to_db(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def get_by_name(self, name):
        return self.query.filter_by(name=name)


class User(db.Model, UserMixin, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email = db.Column(db.String(70))
    password_hash = db.Column(db.Integer)
    events = db.relationship('Event', backref='users', lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password_data):
        return check_password_hash(self.password_hash, password_data)

    @classmethod
    def find_by_email(cls, temp_email):
        email = cls.query.filter_by(email=temp_email).first()
        if email:
            return email


class Event(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    images = db.relationship('Image', backref='event', lazy=True)

    def __init__(self, event_id, title, content, user_id):
        self.id = event_id
        self.title = title
        self.content = content
        self.user_id = user_id


class Image(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(256), index=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))

    def __init__(self, path, event_id):
        self.path = path
        self.event_id = event_id





