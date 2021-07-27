from flask import (Blueprint)

bp = Blueprint('geocode', __name__, url_prefix='/geocode')

@bp.route('/')
def index():
    return "Welcome To Geocode"