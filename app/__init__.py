from flask_restplus import Api
from flask import Blueprint

from .main.controllers.buyer_controller import api as buyer_ns
from .main.controllers.buyer_auth_controller import api as buyer_auth_ns
from .main.controllers.seller_controller import api as seller_ns
from .main.controllers.seller_auth_controller import api as seller_auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restplus web service'
          )

api.add_namespace(buyer_ns, path='/buyer')
api.add_namespace(buyer_auth_ns)
api.add_namespace(seller_ns, path='/seller')
api.add_namespace(seller_auth_ns)