from flask import render_template, url_for,redirect, request
from app.Models import User
from flask_login import current_user, login_user

class LoginController:
	# function handle show form login
	@staticmethod
	def showLoginFrom(error):
		print(current_user)
		return render_template('auth/login.html', error = error)
	def login():
		user = User.query.filter_by(username=request.form['username']).first()
		if user and user.checkPasswordHash(request.form['password']):
			login_user(user)
			return redirect(url_for('.index'))
		else:
			error = 'invalid'
			return LoginController.showLoginFrom(error)