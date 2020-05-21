import uuid
import datetime

from app.main import db
from app.main.models.buyer import Buyer


def save_new_buyer(data):
    buyer = Buyer.query.filter_by(email=data['email']).first()
    if not buyer:
        new_buyer = Buyer(
            public_id = str(uuid.uuid4()),
            first_name = data['first_name'],
            last_name = data['last_name'],
            contact_no = data['contact_no'],
            address = data['address'],
            username = data['username'],
            email = data['email'],
            password = data['password'],
            registered_on = datetime.datetime.utcnow()
        )
        save_changes(new_buyer)
        
        return generate_token(new_buyer)
    else:
        response_object = {
            'status': 'fail',
            'message': 'buyer already exists. Please Log in.',
        }
        return response_object, 409


def get_all_buyers():
    return Buyer.query.all()


def get_a_buyer(public_id):
    return Buyer.query.filter_by(public_id=public_id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()

def generate_token(buyer):
        try:
            # generate the auth token
            auth_token = buyer.encode_auth_token(buyer.public_id)
            response_object = {
                'status': 'success',
                'message': 'Successfully registered.',
                'Authorization': auth_token.decode()
            }
            return response_object, 201
        except Exception as e:
            response_object = {
                'status': 'fail',
                'message': 'Some error occurred. Please try again.'
            }
            return response_object, 401