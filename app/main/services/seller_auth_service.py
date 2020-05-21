from app.main.models.seller import Seller
from app.main.models.seller_blacklist import SellerBlacklistToken
from ..services.seller_blacklist_service import save_token


class SellerAuth:
    @staticmethod
    def login_seller(data):
        try:
            seller = Seller.query.filter_by(username=data.get("username_or_email")).first()

            if seller and seller.check_password(data.get("password")):
                token = seller.encode_token(seller.public_id)

                if token:
                    response_object = {
                        "status": "success",
                        "message": "Successfully logged in.",
                        "Authorization": token.decode()
                    }

                    return response_object, 200

                response_object = {
                    "status": "fail",
                    "message": "There is a server error. Try again later."
                }

                return response_object, 500

            elif seller:
                response_object = {
                    "status": "fail",
                    "message": "Log in unsuccessful. Please try again.",
                }

                return response_object, 401

            else:
                seller = Seller.query.filter_by(email=data.get("username_or_email")).first()

                if seller and seller.check_password(data.get("password")):
                    token = seller.encode_token(seller.public_id)

                    if token:
                        response_object = {
                            "status": "success",
                            "message": "Successfully logged in.",
                            "Authorization": token.decode()
                        }

                        return response_object, 200

                    response_object = {
                        "status": "fail",
                        "message": "There is a server error. Try again later."
                    }

                    return response_object, 500

                response_object = {
                    "status": "fail",
                    "message": "Log in unsuccessful. Please try again."
                }

                return response_object, 401

        except Exception as e:
            response_object = {
                "status": "fail",
                "message": "There is a server error. Try again later."
            }

            return response_object, 500

    @staticmethod
    def logout_user(data):
        try:
            if data.split(" ")[0] == "Bearer":
                token = data.split(" ")[1]
                decode_token = Seller.decode_token(token)
                print(decode_token)
                if decode_token[0]["status"] == "success": 
                    return save_token(token)

                response_object = {
                    "status": "fail",
                    "message": "Provide a valid authorization token."
                }

                return response_object, 401
            
            response_object = {
                "status": "fail",
                "message": "You have issued an illegal or malformed request."
            }

            return response_object, 400

        except Exception as e:
            response_object = {
                "status": "fail",
                "message": "There is a server error. Try again later."
            }

            return response_object, 500


    @staticmethod
    def get_logged_in_seller(data):
        is_token_verified = Seller.decode_token(data)

        if is_token_verified[0]["status"] == "success":
            return Seller.query.filter_by(public_id=is_token_verified[0]["payload"]).first()
        
        return None