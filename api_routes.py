from flask import jsonify, Response

from flask_restful import Resource 
from fetcher_class import FetcherClass, VerifierClass

class ClaimResourceProvider (Resource):
    def get (self, claim_id,prov_id):
        if isinstance(claim_id, str):

            return FetcherClass.fetch_claim_provider (claim_id,prov_id)

        else:

            return Response({ 'message': 'Invalid claim ID.'}, status = 403)

class ClaimStatusResourceProvider(Resource):

    def get (self,claim_id, prov_id):

        if isinstance(claim_id, str):

            return FetcherClass. fetch_claim_status_provider (claim_id,prov_id)

        else:

            return { 'message': 'Invalid claim ID.'}, 403

class ClaimResourceInsurer(Resource):

    def get(self, claim_id, ins_id):

        if isinstance(claim_id, str):

            return FetcherClass.fetch_claim_insurer(claim_id, ins_id)

        else:

            return {'message': 'Invalid claim ID.'}, 403

class ClaimStatusResourceInsurer (Resource):
    def get (self,claim_id, ins_id):

        if isinstance(claim_id,str):

            return FetcherClass.fetch_claim_status_insurer(claim_id, ins_id)

        else:

            return {'message': 'Invalid claim ID.'}, 403

class ProviderIDVerification(Resource):

    def get (self,prov_id):

        if isinstance(prov_id,str): return VerifierClass.verify_prov_status(prov_id)

        else:

            return {'message': 'Invalid Provider ID.'}, 403

class InsurerIDVerification(Resource):

    def get (self, ins_id):

        if isinstance(ins_id, str):
            return VerifierClass.verify_ins_status(ins_id)

        else:
            return {'Invalid Provider ID.'}, 403