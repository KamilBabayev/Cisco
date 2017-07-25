#!/usr/bin/env python3
from flask_sqlalchemy import SQLAlchemy
from server import app
from model import db
from model import User
from model import Command

db = SQLAlchemy(app)
db.create_all()

admin = User('admin', 'admin123')

db.session.add(admin)
db.session.commit()


