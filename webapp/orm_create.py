from models import db
from models import User
from models import Command
from models import Device
from models import ConnUser

db.create_all()
db.session.commit()

'''
admin = User('admin', 'admin123')
db.session.add(admin)
db.session.commit()

showintstatus = Command('show interface status', 'Show Interface Status', 'Show status of Interfaces')
showversion = Command('show version', 'Show IOS Version', 'Show IOS Version')
showipintbrf = Command('show ip interface brief', 'show ip interface brief', 'Shows interface info as brief form')
showmactable = Command('show mac address-table', 'show mac address-table', 'Shows MAC TABLE OF CISCO Device')
showprocmem = Command('show  processes memory', 'SHOW MEM PROCESSES', 'This command show memory info of device')

testcoresw01 = Device('10.50.5.57', 'testswitch01', 'Switch belongs to NetworkTestTeam')
testcoresw02 = Device('10.50.5.57', 'ganja_coresw01', 'GanjaOffice Core Primary Switch')

connuser = ConnUser('cisco', 'cisco')

db.session.add(showversion)
db.session.add(showintstatus)
db.session.add(showipintbrf)
db.session.add(showmactable)
db.session.add(showprocmem)
db.session.add(connuser)
db.session.commit()

db.session.add(testcoresw01)
db.session.add(testcoresw02)
db.session.commit()
'''
