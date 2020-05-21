from flask import request
from flask_restplus import Resource

from app.main.services.seller_auth_service import SellerAuth
from ..util.dtos import SellerAuthDto
from ..util.decorators import seller_token_required

api = SellerAuthDto.api
seller_auth = SellerAuthDto.seller_auth


@api.route("/login")
class SellerLogin(Resource):
    @api.doc("seller log in")
    @api.expect(seller_auth, validate=True)
    def post(self):
        data = request.json

        if data:
            return SellerAuth.login_seller(data)

        response_object = {
            "status": "fail",
            "message": "You have issued an illegal or malformed request."
        }

        return response_object, 400

@api.route("/logout")
class LogoutAPI(Resource):
    @api.doc("seller log out")
    def post(self):
        data = request.headers.get("Authorization")

        if data:
            return SellerAuth.logout_user(data)
        
        response_object = {
            "status": "fail",
            "message": "You have issued an illegal or malformed request."
        }

        return response_object, 400