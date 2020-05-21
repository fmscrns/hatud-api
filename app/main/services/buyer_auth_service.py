from app.main.models.buyer import Buyer
from ..services.buyer_blacklist_service import save_token


class BuyerAuth:
    @staticmethod
    def login_buyer(data):
        try:
            # fetch the buyer data
            buyer = Buyer.query.filter_by(username=data.get('username_or_email')).first()
            if buyer and buyer.check_password(data.get('password')):
                auth_token = buyer.encode_auth_token(buyer.public_id)

                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200

            elif buyer is None:
                buyer = Buyer.query.filter_by(email=data.get('username_or_email')).first()
                if buyer and buyer.check_password(data.get('password')):
                    auth_token = buyer.encode_auth_token(buyer.public_id)

                    if auth_token:
                        response_object = {
                            'status': 'success',
                            'message': 'Successfully logged in.',
                            'Authorization': auth_token.decode()
                        }
                        return response_object, 200

                else:
                    response_object = {
                        'status': 'fail',
                        'message': 'email or password does not match.'
                    }
                    return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500

    @staticmethod
    def logout_buyer(data):
        if data:
            auth_token = data.split(" ")[1]
        else:
            auth_token = ''
        if auth_token:
            resp = Buyer.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # mark the token as blacklisted
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403

    @staticmethod
    def get_logged_in_buyer(new_request):
        auth_token = new_request.headers.get('Authorization')
        resp = Buyer.decode_auth_token(auth_token)
        return Buyer.query.filter_by(public_id=resp).first()