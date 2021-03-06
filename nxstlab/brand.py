from mongoengine import Document
from mongoengine import StringField, EmailField, BooleanField
from flask_login import UserMixin


class Brand(UserMixin, Document):
    company_name = StringField(max_length=60, required=True)
    address = StringField(max_length=120, required=True)
    email = EmailField(required=True, unique=True)
    password = StringField(min_length=6, max_length=60, required=True)
    confirm_password = StringField(min_length=6, max_length=60, required=True)
    isapproved = BooleanField(null=False, default=False)
    isactive = BooleanField(null=False, default=False)
    image = StringField(required=False, default='/static/uploads/brand_profile/default.jpg')