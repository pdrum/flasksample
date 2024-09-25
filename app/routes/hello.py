# app/routes/auth_routes.py
from flask import Blueprint

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/', methods=['GET'])
def hello():
    return 'Hello World!'
