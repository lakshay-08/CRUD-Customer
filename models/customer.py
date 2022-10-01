from flask_sqlalchemy import SQLAlchemy
from app import app
import os

app.config['SQLALCHEMY_DATABASE_URI'] = ''
db = SQLAlchemy(app)


class Customer(db.Model):
    __tablename__ = "customers"
    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    email = db.Column(db.String(255))
