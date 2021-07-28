from flask import (Blueprint, jsonify)

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
    data = {
        "status": "success",
        "body": "Welcome  to Home"
    }
    return jsonify(data)