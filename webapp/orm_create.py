# This script is intended for first time database
# creation and preparation


from models import db
from models import User

db.create_all()
admin = User('admin', 'admin123')
db.session.add(admin)
db.session.commit()

