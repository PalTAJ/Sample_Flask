# import uuid
# import datetime
# import json
#
# from sqlalchemy import and_, or_
# from sqlalchemy.types import Float
# from sqlalchemy.dialects.postgresql import JSON
# from flask_sqlalchemy import SQLAlchemy, BaseQuery
# # from flask_jwt import jwt_required, current_identity, _jwt_required

from .app import app
from flask_mongoengine import MongoEngine


db = MongoEngine()
db.init_app(app)

# database columns will be here

class User(db.Document):
    name = db.StringField()
    password = db.StringField()
    gsm = db.StringField()
    clicked_promotions = db.DictField()
    location = db.PointField()

    def to_json(self):
        return {"name": self.name,
                "email": self.email,
                'password':self.password,
                'gsm': self.gsm,
                'clicked_promotions':self.clicked_promotions,
                'location':self.location}

class Restaurants(db.Document):
    name = db.StringField()
    email = db.StringField()
    gsm = db.StringField()
    description= db.DictField()
    reviews = db.DictField()
    promotions = db.DictField()
    location = db.PointField()
    tags= db.DictField()

    def to_json(self):
        return {"name": self.name,
                "email": self.email,
                'gsm':self.gsm,
                'description':self.description,
                'reviews':self.reviews,
                'promotions':self.promotions,
                'tags':self.tags,
                'location':self.location}

        # pfeJSON = {}
        # pfeJSON['id'] = str(self.id)
        # pfeJSON['point'] = self.location['location']
        # pfeJSON['name'] = str(self.name)
        # return pfeJSON

class Locations(db.Document):
    restaurants_name = db.StringField()
    restaurants_id = db.StringField()
    location = db.PointField()

    def to_json(self):
        return {"restaurants_name": self.restaurants_name,
                "restaurants_id": self.restaurants_id,
                'location':self.location}


class Promotions(db.Document):

    restaurants_id = db.StringField()
    views_counter = db.IntField()
    promotions = db.DictField()
    start_date = db.DateTimeField()
    end_date = db.DateTimeField()
    promotion_hours= db.DictField()

    def to_json(self):
        return {
                "restaurants_id": self.restaurants_id,
                'views_counter': self.views_counter,
                'promotions': self.promotions,
                'start_date':self.start_date,
                'end_date':self.end_date,
                'promotion_hours':self.promotion_hours}