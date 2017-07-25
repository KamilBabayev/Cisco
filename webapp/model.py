from server import app
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, username, password):
        self.username = username
        self.password = password


class Command(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    command = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(80), unique=True)
    desc = db.Column(db.String(500), unique=True)

    def __init__(self, command, name, desc):
        self.command = command
        self.name = name
        self.desc = desc


db.create_all()
