from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class User(db.Model):

    __tablename__='users'
	
    def __init__(self, user, password):
           self.user=user
           self.password=password
	
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(66))
    created_date =db.Column(db.DateTime, default=datetime.datetime.now)
    def verifyPassword(self, password):
         return (self.password ==password)
