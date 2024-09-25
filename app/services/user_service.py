import datetime
from dataclasses import dataclass

import jwt
from flask import current_app
from werkzeug.security import generate_password_hash

from app.daos.user_dao import UserDAO


@dataclass
class AuthAttempt:
    username: str
    password: str


@dataclass
class JwtResponse:
    token: str


def register_user(auth_attempt: AuthAttempt) -> JwtResponse:
    if UserDAO.get_user_by_username(auth_attempt.username):
        raise ValueError("Username already exists")

    UserDAO.create_user(username=auth_attempt.username, password_hash=generate_password_hash(auth_attempt.password))

    return JwtResponse(_create_jwt_token(auth_attempt.username))


def login(auth_attempt: AuthAttempt) -> JwtResponse:
    user = UserDAO.get_user_by_username(auth_attempt.username)

    if not user or not user.check_password(auth_attempt.password):
        raise ValueError("Invalid username or password")

    return JwtResponse(_create_jwt_token(auth_attempt.username))


def _create_jwt_token(username: str) -> str:
    # Set expiration time for the token
    expiration = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    # JWT payload
    payload = {
        "sub": username,
        "exp": expiration
    }

    # Secret key (you should set this in your Flask config)
    secret_key = current_app.config['SECRET_KEY']

    # Generate token
    token = jwt.encode(payload, secret_key, algorithm="HS256")

    return token
