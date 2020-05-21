from flask_restplus import Namespace, fields


class BuyerDto:
    api = Namespace('buyer', description='buyer related operations')
    buyer = api.model('buyer', {
        'public_id': fields.String(description='buyer identifier'),
        'first_name' : fields.String(required=True, description='buyer first name'),
        'last_name' : fields.String(required=True, description='buyer last name'),
        'contact_no' : fields.String(required=True, description='buyer contact number'),
        'address' : fields.String(required=True, description='buyer address'),
        'username': fields.String(required=True, description='buyer username'),
        'email': fields.String(required=True, description='buyer email address'),
        'password': fields.String(required=True, description='buyer password')
    })

class BuyerAuthDto:
    api = Namespace('buyer', description='buyer authentication related operations')
    buyer_auth = api.model('buyer_auth_details', {
        'username_or_email' : fields.String(required=True, description='buyer username or email address'),
        'password': fields.String(required=True, description='buyer password'),
    })

class SellerDto:
    api = Namespace('seller', description='seller related operations')
    seller = api.model('seller', {
        'public_id': fields.String(description='seller identifier'),
        'first_name' : fields.String(required=True, description='seller name'),
        'last_name' : fields.String(required=True, description='seller last name'),
        'contact_no' : fields.String(required=True, description='seller contact number'),
        'address' : fields.String(required=True, description='seller address'),
        'username': fields.String(required=True, description='seller username'),
        'email': fields.String(required=True, description='seller email address'),
        'password': fields.String(required=True, description='seller password')
    })

class SellerAuthDto:
    api = Namespace('seller', description='seller authentication related operations')
    seller_auth = api.model('seller_auth_details', {
        'username_or_email' : fields.String(required=True, description='seller username or email address'),
        'password': fields.String(required=True, description='seller password'),
    })