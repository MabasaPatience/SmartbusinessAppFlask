from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(150))
    last_name=db.Column(db.String(150))
    email=db.Column(db.String(150),unique=True)
    gender=db.Column(db.String(150))
    identity=db.Column(db.String(150))
    tel=db.Column(db.String(150))
    type=db.Column(db.String(150))
    password=db.Column(db.String(150))
    Company=db.relationship('Company')
    Post=db.relationship('Post')
    Address=db.relationship('Address')
    Prediction=db.relationship('Prediction')




class Company(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(150))
    reg_no=db.Column(db.String(150),unique=True)
    email=db.Column(db.String(150),unique=True)
    discription=db.Column(db.String(150))
    date_created=db.Column(db.DateTime(timezone=True),default=func.now)
    type_Business=db.Column(db.String(150))
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))



class Post(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(150))
    Comment=db.Column(db.String(150))
    date_posted=db.Column(db.DateTime,default=datetime.utcnow)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    

class Address(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    street_name=db.Column(db.String(150))
    town=db.Column(db.String(150))
    province=db.Column(db.String(150))
    postal_code=db.Column(db.Integer)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))

class Prediction(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(150))
    Store_Area=db.Column(db.Integer)
    Items_Available=db.Column(db.Integer)
    Customer_count=db.Column(db.Integer)
    sale_prediction=db.Column(db.Integer)
    date_created=db.Column(db.DateTime(timezone=True),default=func.now)
    user_id=db.Column(db.Integer,db.ForeignKey('user.id'))
    

