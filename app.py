from flask import Flask,request,jsonify
from flask_restful import Api, Resource
from api_routes import ClaimResourceProvider, ClaimStatusResourceProvider, ClaimResourceInsurer, ClaimStatusResourceInsurer
from api_routes import ProviderIDVerification, InsurerIDVerification


app = Flask(__name__)
api = Api(app)

api.add_resource(ClaimResourceProvider, '/provider/<prov_id>/claims/<claim_id>')
api.add_resource(ClaimStatusResourceProvider, '/provider/<prov_id>/claims/status/<claim_id>')
api.add_resource(ClaimResourceInsurer, '/insurer/<ins_id>/claims/<claim_id>')
api.add_resource(ClaimStatusResourceInsurer, '/insurer/<ins_id>/claims/status/<claim_id>')
api.add_resource(ProviderIDVerification, '/provider/<prov_id>')
api.add_resource(InsurerIDVerification, '/insurer/<ins_id>')



if __name__ == '__main__':
    app.run(debug=True)