import uuid
import datetime

from app.main import db
from app.main.models.seller import Seller


def save_new_seller(data):
    seller = Seller.query.filter_by(email=data["email"]).first()
    if not seller:
        new_seller = Seller(
            public_id = str(uuid.uuid4()),
            first_name = data["first_name"],
            last_name = data["last_name"],
            contact_no = data["contact_no"],
            address = data["address"],
            username = data["username"],
            email = data["email"],
            password = data["password"],
            registered_on = datetime.datetime.utcnow()
        )
        save_changes(new_seller)
        
        return generate_token(new_seller)
    else:
        response_object = {
            "status": "fail",
            "message": "Seller already exists. Please log in.",
        }
        return response_object, 409


def get_all_sellers():
    return Seller.query.all()


def get_a_seller(public_id):
    return Seller.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def generate_token(seller):
        try:
            # generate the auth token
            auth_token = seller.encode_auth_token(seller.public_id)
            response_object = {
                "status": "success",
                "message": "Seller registered successfully.",
                "Authorization": auth_token.decode()
            }
            return response_object, 201
        except Exception as e:
            response_object = {
                "status": "fail",
                "message": "Some error occurred. Please try again."
            }
            return response_object, 401