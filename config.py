import os

#config database
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:18031997@localhost/python"
SQLALCHEMY_TRACK_MODIFICATIONS = True
# Secret key for signing cookies
# SECRET_KEY = os.urandom(16)
SECRET_KEY = "Test"