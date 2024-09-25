from dataclasses import dataclass


@dataclass
class AuthAttempt:
    username: str
    password: str


@dataclass
class JwtResponse:
    token: str


def register_user(auth_attempt: AuthAttempt) -> JwtResponse:
    return JwtResponse("")
