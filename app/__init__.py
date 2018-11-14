import click
from flask_script import Manager
from flask import Flask, render_template, g, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate, MigrateCommand
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, current_user

# initialize the app
app = Flask(__name__,
	static_folder 	= '../public',
	static_url_path = '', 
	template_folder = '../resources/views'
)
#load config 
app.config.from_object('config')
#connect bcrypt to app and login
bcrypt = Bcrypt(app)
login = LoginManager(app)

#connect database
db = SQLAlchemy(app)
ma = Marshmallow(app)
#import models to app
from app.Models import *
#connect database with migrate
migrate = Migrate(app, db)
#command
manager = Manager(app)
manager.add_command('db', MigrateCommand)

#share view
@app.context_processor
def inject_user():
    return dict(user="Nguyen Manh")

# register bludeprint
from routes.web import web
from routes.api import api_v1
app.register_blueprint(web, url_prefix='')
app.register_blueprint(api_v1, url_prefix='/api/v1')


# function handle errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html')

@app.before_request
def before_request():
    g.user = current_user

#handle login
@login.unauthorized_handler
def unauthorized():
    # do stuff
    return redirect('/login')