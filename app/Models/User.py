from app import db, ma, bcrypt, login
from flask_login import UserMixin

class User(UserMixin, db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), nullable=False)
	password = db.Column(db.String(255), nullable=False)
	username = db.Column(db.String(120), unique=True, nullable=False)
	email = db.Column(db.String(255), unique=True, nullable=False)
	email_verified_at = db.Column(db.TIMESTAMP(), nullable=True)
	remember_token = db.Column(db.String(120), nullable=True)
	created_at = db.Column(db.TIMESTAMP(), nullable=True, server_default=db.func.now())
	updated_at = db.Column(db.TIMESTAMP(), nullable=True, server_default=db.func.now(), server_onupdate=db.func.now())

	#convert to string
	def __repr__(self):
		return str(self.__dict__)
	#genarate hash pasword
	def generatePasswordHash(password):
		return bcrypt.generate_password_hash(password, 10)
	def checkPasswordHash(self, password):
		return bcrypt.check_password_hash(self.password, password)

#Tạo Schema cho model
class UserSchema(ma.ModelSchema):
	class Meta:
		fields = ('id','username','email', 'created_at', 'updated_at')