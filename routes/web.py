#import flask
from flask import Blueprint
#import controller
from app.Http.Controllers.HomeController import HomeController
#define web blueprint
web = Blueprint('',__name__)

# page home /
@web.route('/')
def index():
	return HomeController.index()
#page about
@web.route('/about')
def about():
	return HomeController.about()