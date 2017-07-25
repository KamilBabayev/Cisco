#!/usr/bin/env python3
from model import User
from model import db

admin  = User('admin', 'admin123')
db.session.add(admin)
db.session.commit()




