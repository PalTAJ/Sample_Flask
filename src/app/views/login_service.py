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



@app.route('/add-users', methods=['POST', 'GET'])
def add_user():
    User(name='taj',
         location=[41.01792397981938,29.02027964232864]).save()
    return {200:'Done'}


@app.route('/search-users', methods=['POST', 'GET'])
def search_users():
    user = User.objects(name="taj").first()
    # print(user)
    return {200:user}



@app.route('/add-rest', methods=['POST', 'GET'])
def add_rest():


## adding two resturants with different locations, one is 1000 meters away, while pizza hut is 1700 meter away


    Restaurants(
        name='pizza hut',
        email='pizza.hot@gmail.com',
        gsm='05432432423',
        promotions ={'type':"pizza",'price':60,'discount': '50%','new_price':30},
        location={'type': 'Point','coordinates': [41.020729347122554, 29.03533618565567]}
    ).save()

    Restaurants(
        name='burger king',
        email='burger.king@gmail.com',
        gsm='05432432423',
        promotions ={'type':"burger",'price':50,'discount': '50%','new_price':25},
        location={'type': 'Point','coordinates': [41.023548030278604, 29.01539231232764] }
    ).save()

    return {200:'Done'}




@app.route('/add-prom', methods=['POST', 'GET'])
def add_prom():

    sDate = parse("23-3-2021 00-00", fuzzy=True)
    eDate = parse("23-4-2021 00-00", fuzzy=True)

    Promotions(restaurants_id ='6063a191a631e743c5df0ab4',
               views_counter =1,
               promotions = {'type':"burger",'price':50,'discount': '50%','new_price':25},
               start_date = sDate,
               end_date = eDate,
               promotion_hours= {'start':'12:00','end':'20:00'}
               ).save()


    sDate = parse("23-4-2021 00-00", fuzzy=True)
    eDate = parse("23-5-2021 00-00", fuzzy=True)

    Promotions(restaurants_id ='6063a191a631e743c5df0ab4',
               views_counter =1,
               promotions = {'type':"burger",'price':50,'discount': '75%','new_price':12.5},
               start_date = sDate,
               end_date = eDate,
               promotion_hours = {'start': '12:00', 'end': '20:00'}

               ).save()

    sDate = parse("01-3-2021 00-00", fuzzy=True)
    eDate = parse("15-3-2021 00-00", fuzzy=True)

    Promotions(restaurants_id ='6063a191a631e743c5df0ab4',
               views_counter =1,
               promotions = {'type':"burger",'price':100,'discount': '25%','new_price':75},
               start_date = sDate,
               end_date = eDate,
               promotion_hours = {'start': '12:00', 'end': '20:00'}

    ).save()


    sDate = parse("23-3-2021 00-00", fuzzy=True)
    eDate = parse("23-4-2021 00-00", fuzzy=True)

    Promotions(restaurants_id ='6063a191a631e743c5df0ab3',
               views_counter =1,
               promotions = {'type':"pizza",'price':50,'discount': '50%','new_price':25},
               start_date = sDate,
               end_date = eDate,
               promotion_hours = {'start': '12:00', 'end': '20:00'}

               ).save()



    return {200:'Success'}


@app.route('/search-rest', methods=['POST', 'GET'])
def search_rest():

    user = Restaurants.objects(location__near=[41.01792397981938,29.02027964232864], location__max_distance=1700)

    return {200: user}


@app.route('/search-prom', methods=['POST', 'GET'])
def search_prom():

    promo = []

    sDate = parse("25-03-2021 13-00", fuzzy=True)  # format the date and time
    sHour = sDate.strftime('%H:%M')  ## extract hour and minuts

    res = Restaurants.objects(location__near=[41.01792397981938,29.02027964232864], location__max_distance=1000).only('name')  ## checks rest near me
    for re in res:

        id = str(re.to_mongo().to_dict()['_id'])  ## find resturants ids that are within location range
        prom = Promotions.objects(restaurants_id=id)

        pro = prom(__raw__=
            {
                'start_date':{"$lte": sDate }, ## if current provided date is less than or equal query
                'end_date': {"$gt": sDate}, # if current provided date is greater than query
                'promotion_hours.start':{'$lte': sHour}, #if start is less or equal than 13:00
                'promotion_hours.end': {'$gt': sHour}, # if end is larger than 19:00
                'promotions.type': 'burger'  #checks promotion type of food
            })

        promo.append(pro)


    return {200:promo}



