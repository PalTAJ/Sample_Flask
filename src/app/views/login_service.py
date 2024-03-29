from flask import jsonify, request
from flask import Flask, render_template
from ..schemas import *
from ..app import app
from ..models import db,User, Restaurants, Promotions

import marshmallow


from dateutil.parser import parse
from datetime import datetime as dt


@app.route('/login', methods=['POST', 'GET'])
def Login():

    try:
        data = LoginSchema().load(request.json)

    except marshmallow.exceptions.ValidationError as error:
        return {400:'Bad Request'}
    if not request.json:
        return {404:'not found'}

    print(data)

    return {'200':'ok'}


