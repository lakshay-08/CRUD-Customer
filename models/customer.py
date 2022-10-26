try:
    from flask_sqlalchemy import SQLAlchemy
except Exception as e:
    print("Some packages are missing :", e)

db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = "customer"

    customer_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    phone_number = db.Column(db.String(255))
    email = db.Column(db.String(255))

    def __init__(self, first_name, last_name, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.email = email
