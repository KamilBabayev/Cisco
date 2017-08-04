from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
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
    desc = db.Column(db.String(300), unique=True)

    def __init__(self, command, name, desc):
        self.command = command
        self.name = name
        self.desc = desc

class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.String(20), unique=False)
    name = db.Column(db.String(200), unique=True)
    desc = db.Column(db.String(300), unique=True)

    def __init__(self, ip, name, desc):
        self.ip = ip
        self.name = name
        self.desc = desc

class ConnUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, username, password):
        self.username = username
        self.password = password

#db.create_all()
