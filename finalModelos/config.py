import os
class config(object):
	SECRET_KEY = 'llave_de_pepito'
	
class DevelopmentConfig(config):
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Vgyrock_444666@localhost/flask'
	SQLALCHEMY_TRACK_MODIFICATIONS =False