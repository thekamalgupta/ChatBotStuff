from flask import jsonify, Response
from cosmosdb_conn import DB_Query

class FetcherClass:
    
    def fetch_claim_provider(claim_id, prov_id):
        claim = DB_Query.get_claim_details_provider(claim_id,prov_id)
        if claim:
            return {\
                'claimid':claim['ClaimID'],\
                'ProvName':claim['ProvName'],\
                'ProvPymt':claim['ProvPymt'],\
                'ProvCode':claim['ProvCode']\
                }, 200
        else:
            return {'message': 'No Claim found'}, 404
            
    
    def fetch_claim_status_provider(claim_id, prov_id):
        claim = DB_Query.get_claim_status_provider(claim_id, prov_id)
        
        if claim:
            return {\
                'claimid':claim['ClaimID'],\
                'Claim Status':claim['ProvCode']\
                }, 200
        else:
            return {'message': 'No Claim found'}, 404
            
            
    
    def fetch_claim_insurer(claim_id, ins_id):
        claim = DB_Query.get_claim_details_insurer(claim_id,ins_id)
        if claim:
            return {\
                'claimid':claim['ClaimID'],\
                'ProvName':claim['ProvName'],\
                'ProvPymt':claim['ProvPymt'],\
                'ProvCode':claim['ProvCode']\
                }, 200
        else:
            return {'message': 'No Claim found'}, 404  
            
            
            
    def fetch_claim_status_insurer(claim_id, ins_id):
        claim = DB_Query.get_claim_status_insurer(claim_id, ins_id)
        
        if claim:
            return {\
                'claimid':claim['ClaimID'],\
                'Claim Status':claim['InsCode']\
                }, 200
        else:
            return {'message': 'No Claim found'}, 404 
            
            
class VerifierClass:
    
    def verify_prov_status(prov_id):
        prov = DB_Query.get_provider(prov_id)
        if prov:
            return {'message': 'Verified Successfully'}, 201
            
        else:
            return {'message':'Invalid Provider ID'}, 403
            
    def verify_ins_status(ins_id):
        ins = DB_Query.get_insurer(ins_id)
        if ins:
            return {'message': 'Verified Successfully'}, 201
            
        else:
            return {'message':'Invalid Provider ID'}, 403