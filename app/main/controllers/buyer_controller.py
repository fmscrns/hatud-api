from flask import request
from flask_restplus import Resource

from ..util.dtos import BuyerDto
from ..services.buyer_service import save_new_buyer, get_all_buyers, get_a_buyer
from app.main.services.buyer_auth_service import BuyerAuth

api = BuyerDto.api
_buyer = BuyerDto.buyer


@api.route('/')
class BuyerList(Resource):
    @api.doc('get current buyer')
    @api.marshal_with(_buyer)
    def get(self):
        """get current buyer given its token"""
        return BuyerAuth.get_logged_in_buyer(request)

    @api.response(201, 'Buyer successfully created.')
    @api.doc('create a new buyer')
    @api.expect(_buyer, validate=True)
    def post(self):
        """Creates a new Buyer """
        data = request.json
        return save_new_buyer(data=data)