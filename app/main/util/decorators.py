from functools import wraps
from flask import request

from app.main.services.buyer_auth_service import BuyerAuth
from app.main.services.seller_auth_service import SellerAuth



def buyer_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = BuyerAuth.get_logged_in_user(request)
        token = data.get("data")

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated

def seller_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = SellerAuth.get_logged_in_user(request)
        token = data.get("data")

        if not token:
            return data, status

        return f(*args, **kwargs)

    return decorated

