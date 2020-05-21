import datetime, jwt
from app.main.models.buyer_blacklist import BuyerBlacklistToken
from ..db_config import key
from .. import db, flask_bcrypt


class Buyer(db.Model):
    """ Buyer Model for storing buyer related details """
    __tablename__ = "buyer"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    public_id = db.Column(db.String(100), unique=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    contact_no = db.Column(db.String(20), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(100))
    registered_on = db.Column(db.DateTime, nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<Buyer '{}'>".format(self.username)

    def encode_auth_token(self, customer_id):
            """
            Generates the Auth Token
            :return: string
            """
            try:
                payload = {
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                    'iat': datetime.datetime.utcnow(),
                    'sub': customer_id
                }
                return jwt.encode(
                    payload,
                    key,
                    algorithm='HS256'
                )
            except Exception as e:
                return e

    @staticmethod  
    def decode_auth_token(auth_token):
            """
            Decodes the auth token
            :param auth_token:
            :return: integer|string
            """
            try:
                payload = jwt.decode(auth_token, key)
                is_blacklisted_token = BuyerBlacklistToken.check_blacklist(auth_token)
                if is_blacklisted_token:
                    return 'Token blacklisted. Please log in again.'
                else:
                    return payload['sub']
            except jwt.ExpiredSignatureError:
                return 'Signature expired. Please log in again.'
            except jwt.InvalidTokenError:
                return 'Invalid token. Please log in again.'
