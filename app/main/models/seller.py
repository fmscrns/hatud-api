import datetime, jwt
from app.main.models.seller_blacklist import SellerBlacklistToken
from ..db_config import key
from .. import db, flask_bcrypt


class Seller(db.Model):
    """ Seller Model for storing seller related details """
    __tablename__ = "seller"

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
        return "<Seller '{}'>".format(self.username)

    def encode_token(self, seller_id):
            """
            Generates the Auth Token
            :return: string
            """
            try:
                payload = {
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=5),
                    'iat': datetime.datetime.utcnow(),
                    'sub': seller_id
                }
                return jwt.encode(
                    payload,
                    key,
                    algorithm='HS256'
                )
            except Exception as e:
                return e

    @staticmethod  
    def decode_token(token):
            try:
                payload = jwt.decode(token, key)
                
                is_token_blacklisted = SellerBlacklistToken.check_blacklist(token)
                print(is_token_blacklisted)
                if not is_token_blacklisted:
                    response_object = {
                        "status": "success",
                        "message": "Token successfully decoded.",
                        'payload': payload["sub"]
                    }

                    return response_object, 200

                response_object = {
                    "status": "fail",
                    "message": "Please log in again."
                }

                return response_object, 403

            except jwt.ExpiredSignatureError:
                response_object = {
                    "status": "fail",
                    "message": "Provide a valid authorization token."
                }

                return response_object, 403

            except jwt.InvalidTokenError:
                response_object = {
                    "status": "fail",
                    "message": "Provide a valid authorization token."
                }

                return response_object, 401
