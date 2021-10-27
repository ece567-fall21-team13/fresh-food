# coding: utf-8

from flask import Blueprint
from flask_apispec import use_kwargs

from .serializers import order_schema
from ..extensions import db
from ..utils import generate_uuid

from geopy.geocoders import Nominatim
from geopy import distance


blueprint = Blueprint('profiles', __name__)


@blueprint.route('/api/customer/place_oder', methods=('POST',))
@use_kwargs(order_schema)
def place_order(**kwargs):
    drivers_result = db.engine.execute("SELECT * from drivers")
    drivers = []
    restaurants_result = db.engine.execute("SELECT * from restaurants")
    restaurants = []
     #hit the maps api for all the restaurant address and the customer's address.
    # We'll have time in mins for all restaurants for that customer_uuid
    geolocator = Nominatim(user_agent="fresh-food")
    for r in drivers_result:  #Find latitude/longitude of each driver
        row_as_dict = dict(r)
        location = geolocator.geocode(row_as_dict['current_location'])
        row_as_dict['latitude'] = location.latitude
        row_as_dict['longitude'] = location.longitude
        drivers.append(row_as_dict)

    for r in restaurants_result: #Find latitude/longitude of each restaurant
        row_as_dict = dict(r)
        location = geolocator.geocode(row_as_dict['current_location'])
        row_as_dict['latitude'] = location.latitude
        row_as_dict['longitude'] = location.longitude
        restaurants.append(row_as_dict)

    availableDrivers = drivers
    
    for driver in availableDrivers: #assign driver to the restaurant they are closest to and find time to reach
        minDistance = 999999999;
        restaurantIndex = -1;
        for i in range(restaurants.length):
            milage = distance.distance( (driver['latitude'], driver['longitude']), (restaurants[i]['latitude'], restaurants[i]['longitude']) ).miles
            if (milage < minDistance):
                restaurantIndex = i
                minDistance = milage
        
        driver['assigned_restaurant'] = restaurants[restaurantIndex]['name']
        driver['time_to_reach_restaurant'] = 2*distance.distance( (driver['latitude'], driver['longitude']), (restaurants[restaurantIndex]['latitude'], restaurants[restaurantIndex]['longitude']) ).miles #minutes
        availableDrivers.remove(restaurants[restaurantIndex])

    orders_result = db.engine.execute("SELECT orders.order_uuid, customers.name AS cname, customers.address AS address, restaurants.name AS rname FROM customers INNER JOIN orders ON customers.customer_uuid = orders.customer_uuid INNER JOIN restaurants ON orders.restaurant_uuid = restaurants.restaurant_uuid")
    
    orders = []

    for r in order_result:  #Find latitude/longitude of each order
        row_as_dict = dict(r)
        location = geolocator.geocode(row_as_dict['address'])
        row_as_dict['latitude'] = location.latitude
        row_as_dict['longitude'] = location.longitude
        orders.append(row_as_dict)

    for order in orders:
        restaurant_name = order['rname']
        time_to_reach_restaurant = 0
        assigned_restaurant = ''
        for driver in drivers:
            if driver['assigned_restaurant'] == restaurant_name:
                assigned_restaurant = driver['assigned_restaurant']
                time_to_reach_restaurant = driver['time_to_reach_restaurant']
                driverLat = driver['latitude']
                driverLong = driver['longitude']
                break
        time_restaurant_to_order = 0
        for restaurant in restaurants:
            if restaurant['name'] == restaurant_name:
                time_restaurant_to_order = 2*distance.distance( (driverLat, driverLong), (restaurant['latitude'], restaurant['longitude']) ).miles #minutes
                break

        order['time_to_deliver'] = time_to_reach_restaurant + time_restaurant_to_order
   
    freshResult = db.engine.execute("SELECT customer_uuid, order_uuid, restaurant_uuid FROM customers INNER JOIN orders ON customers.customer_uuid = orders.customer_uuid INNER JOIN restaurants ON orders.restaurant_uuid = restaurants.restaurant_uuid")

    #Append time to delivery calculated above to each entry
    for r in freshResult:  
        row_as_dict = dict(r)
        for order in orders:
            if order['order_uuid'] == row_as_dict['order_uuid']:
                row_as_dict['time_delivery'] = order['time_to_deliver']
                break
        drivers.append(row_as_dict)

    return response #With fields customer_id, order_uuid, restaurant_uuid, status, time_delivery
