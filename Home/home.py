from flask import (Blueprint)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    return "Welcome To Home"