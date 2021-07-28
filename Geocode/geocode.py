import os
import requests
import logging
from flask import (Blueprint, jsonify, request, abort)
from utils import haversine

bp = Blueprint('geocode', __name__, url_prefix='/geocode')


@bp.route('/')
def index():
    data = {
        "status": "success",
        "body": "Welcome to Index Geocode"
    }
    return jsonify(data)


@bp.route('/calculate', methods=['POST'])
def calculate():
    if not request.json:
        abort(404)

    search = request.json['search']
    url = "https://geocode-maps.yandex.ru/1.x"
    params = {
        "apikey": os.getenv("API_KEY_GEOLOCATION"),
        "geocode": search,
        "format": "json",
        "lang": "en_US"
    }
    # set logging to save data .logfile
    logging.basicConfig(filename="logfile/{}.log".format(search), format='%(asctime)s %(message)s', filemode='w')
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.info("Searching address/location : {}".format(search))
    logger.info("===========================================")

    res = requests.get(url=url, params=params)
    res_json = res.json()
    data_list = res_json['response']['GeoObjectCollection']['featureMember']

    lat_center = float(os.getenv('LAT_CENTER'))
    lng_center = float(os.getenv('LNG_CENTER'))

    for n in data_list:
        lng_lat = n['GeoObject']['Point']['pos'].split()
        lng_target = float(lng_lat[0])
        lat_target = float(lng_lat[1])
        distance = haversine(lat_center, lng_center, lat_target, lng_target)
        n['GeoObject']['Distance'] = str(distance)
        if distance >= float(os.getenv('R_MKD')):
            logger.info("---------------------------------")
            logger.info("kind : {}".format(n['GeoObject']['metaDataProperty']['GeocoderMetaData']['kind']))
            logger.info("address : {}".format(n['GeoObject']['metaDataProperty']['GeocoderMetaData']['text']))
            logger.info("Longtitude Latitude : {}".format(n['GeoObject']['Point']['pos']))
            logger.info("Distance : {}".format(distance))
            logger.info("----------------------------------")

    data = {
        "status": "success",
        "body": data_list
    }

    return jsonify(data)
