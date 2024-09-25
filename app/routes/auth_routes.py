from flask import Blueprint, request, jsonify
from app.services.user_service import register_user, AuthAttempt, login

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register_api():
    data = request.get_json()
    result = register_user(AuthAttempt(username=data.get('username'), password=data.get('password')))
    return jsonify({"token": result.token}), 201


@auth_bp.route('/login', methods=['POST'])
def login_api():
    data = request.json
    result = login(AuthAttempt(username=data['username'], password=data['password']))
    return jsonify({"token": result.token}), 200

