from flask import request
from flask_restplus import Resource

from app.main.services.buyer_auth_service import BuyerAuth
from ..util.dtos import BuyerAuthDto
from ..util.decorators import buyer_token_required

api = BuyerAuthDto.api
buyer_auth = BuyerAuthDto.buyer_auth


@api.route('/login')
class BuyerLogin(Resource):
    """
        Buyer Login Resource
    """
    @api.doc('buyer login')
    @api.expect(buyer_auth, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return BuyerAuth.login_buyer(data=post_data)

@buyer_token_required
@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """
    @api.doc('logout a buyer')
    def post(self):
        # get auth token
        auth_header = request.headers.get('Authorization')
        return BuyerAuth.logout_buyer(data=auth_header)