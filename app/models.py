from flask_login import UserMixin
from app import mongo

class User(UserMixin):
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def save(self):
        mongo.db.users.insert_one({
            'username': self.username,
            'password': self.password,
            'role': self.role
        })

    @staticmethod
    def find_by_username(username):
        return mongo.db.users.find_one({'username': username})
