#import flask
from flask import Blueprint, request, url_for,redirect
#import controller
from app.Http.Controllers.HomeController import HomeController
from app.Http.Controllers.Auth.LoginController import LoginController
from flask_login import login_required, logout_user
#define web blueprint
web = Blueprint('',__name__)

# page home /
@web.route('/')
@web.route('/home')
@login_required
def index():
	return HomeController.index()
#page about
@web.route('/about')
def about():
	return HomeController.about()

#page login
@web.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
	error = None
	if request.method == 'POST':
		return LoginController.login()
	return LoginController.showLoginFrom(error)

# page logout
@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/login')