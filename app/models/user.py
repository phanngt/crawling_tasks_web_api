from app import db


class User(db.Model):
    __tablename__ = 'Users'
    id = db.Column('Id', db.BigInteger, primary_key=True)
    uuid = db.Column('UUID', db.String(32), nullable=False, default='')
    valid = db.Column('Valid', db.SmallInteger, nullable=False, default=1)
    username = db.Column('Username', db.String(128), nullable=False)
    email = db.Column('Email', db.String(128))
    auth_service = db.Column('AuthService', db.String(32), default=None)
    auth_data = db.Column('AuthData', db.String(256), default=None)
    auth_service_access_token = db.Column('AuthServiceAccessToken', db.String(3072), default=None)

    @staticmethod
    def get(user_id):
        """
        :type user_id: int
        :rtype: User
        """
        user = User.query.get(user_id)
        return user
