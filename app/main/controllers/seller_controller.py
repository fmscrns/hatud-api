from flask import request
from flask_restplus import Resource

from ..util.dtos import SellerDto
from ..services.seller_service import save_new_seller, get_all_sellers, get_a_seller
from app.main.services.seller_auth_service import SellerAuth

api = SellerDto.api
_seller = SellerDto.seller


@api.route('/')
class Seller(Resource):
    @api.doc('get current seller')
    @api.marshal_with(_seller)
    def get(self):
        """get current seller given its token"""
        
        ab = SellerAuth.get_logged_in_seller(request)

        return ab

    @api.response(201, 'Seller successfully created.')
    @api.doc('create a new seller')
    @api.expect(_seller, validate=True)
    def post(self):
        """Creates a new Seller """
        data = request.json
        return save_new_seller(data=data)