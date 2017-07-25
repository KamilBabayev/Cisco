from models import User
users = User.query.all()
admin = User.query.filter_by(username='admin').first()
print(users)
print(admin.username, admin.password)
