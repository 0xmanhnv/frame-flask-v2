from flask import render_template
from app.Models import User
from app import db


class HomeController():
	# function handle index
	def index():
		# user = User()
		# user.password = '$2b$10$j1mggLF7uPvh2B0XfWfPx.zVEV2RUf/uKh8Fj9LTX9tLc9X6cQtRO'
		# if user.checkPasswordHash('123456'):
		# 	return "true"
		# else:
		# 	return "false"
		# 	
		# user = User(username='user', email='user@example.com', password=User.generatePasswordHash('123456'), name='nguyenmanh')
		# db.session.add(user)
		# db.session.commit()
		return render_template('blog/home.html')
	def about():
		return render_template('blog/about.html')