from models import db
from models import User
from models import Command

db.create_all()
admin = User('admin', 'admin123')
db.session.add(admin)
db.session.commit()

showintstatus = Command('show interface status', 'Show Interface Status', 'Show status of Interfaces')
showversion = Command('show version', 'Show IOS Version', 'Show IOS Version')
showipintbrf = Command('show ip interface brief', 'show ip interface brief', 'Shows interface info as brief form')
db.session.add(showversion)
db.session.add(showintstatus)
db.session.add(showipintbrf)
db.session.commit()
