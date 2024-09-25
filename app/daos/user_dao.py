from typing import Optional

from app.models import User, db

class UserDAO:
    @staticmethod
    def get_user_by_username(username: str) -> Optional[User]:
        return User.query.filter_by(username=username).first()

    @staticmethod
    def create_user(username: str, password_hash: str) -> Optional[User]:
        new_user = User(username=username, password_hash=password_hash)
        db.session.add(new_user)
        db.session.commit()
