from flask import render_template
from app.Models import User

class HomeController():
	# function handle index
	def index():
		# user = User()
		# user.password = '$2b$10$j1mggLF7uPvh2B0XfWfPx.zVEV2RUf/uKh8Fj9LTX9tLc9X6cQtRO'
		# if user.checkPasswordHash('123456'):
		# 	return "true"
		# else:
		# 	return "false"
		return render_template('blog/home.html')
	def about():
		return render_template('blog/about.html')