from app.main import db
from app.main.models.seller_blacklist import SellerBlacklistToken


def save_token(data):
    token = SellerBlacklistToken(token=data)

    try:
        db.session.add(token)
        db.session.commit()

        response_object = {
            "status": "success",
            "message": "Successfully logged out."
        }

        return response_object, 200

    except Exception as e:
        response_object = {
            "status": "fail",
            "message": e
        }
        
        return response_object, 400