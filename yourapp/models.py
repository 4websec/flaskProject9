# models.py located at C:\Code\flaskProject9\yourapp\models.py

from .extensions import db
from flask_login import current_user
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(100))
    drug_testing_phone = db.Column(db.String(20))
    ivr_code = db.Column(db.String(20))
    mobile_number1 = db.Column(db.String(20))
    mobile_number2 = db.Column(db.String(20))
    checkin_time = db.Column(db.Time)  # Stores time only
    days_of_week = db.Column(db.String(255))  # Stores days as a comma-separated string

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
