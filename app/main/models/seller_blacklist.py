from .. import db
import datetime


class SellerBlacklistToken(db.Model):
    __tablename__ = "seller_blacklist_tokens"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    token = db.Column(db.String(500), unique=True, nullable=False)
    blacklisted_on = db.Column(db.DateTime, nullable=False)

    def __init__(self, token):
        self.token = token
        self.blacklisted_on = datetime.datetime.now()

    def __repr__(self):
        return "<id: seller token: {}".format(self.token)

    @staticmethod
    def check_blacklist(data):
        token = SellerBlacklistToken.query.filter_by(token=str(data)).first()
        
        if token:
            return True

        return False