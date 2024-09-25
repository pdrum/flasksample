from flask import Blueprint, request, jsonify
from app.services.user_service import register_user, AuthAttempt

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result = register_user(AuthAttempt(username=data.get('username'), password=data.get('password')))
    return jsonify({"token": result.token}), 201
