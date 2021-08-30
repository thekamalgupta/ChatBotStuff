#import necessary libraries

from azure.cosmos import CosmosClient

import os

 # url, key are available at the Azure CosmosDB Portal


url= 'https://azurecosmossql.documents.azure.com:443/'

key= "avNzmOcNxBpyJMng6o6NH58AvBqSgCBNN6NKAhTUUPOdykrBEYawPtc0AGlimBoYSHPDajf3RRXRiXlGfrt86g=="

#client is an instance of Cosmos client, can be named anything

client = CosmosClient(url, credential=key)


database_name = 'MockClaimDB'



database =  client.get_database_client(database_name)

container_name = 'claimcontainer' 
container =  database.get_container_client (container_name)
 #Query the database as required

class DB_Query:

    def get_claim_details_provider(claim_id, prov_id):
        """ To retrieve the details of claim for a provider."""

        q = 'SELECT * FROM mycontainer r WHERE r.ClaimID="{}" AND r.ProvCode = "{}" '.format(claim_id, prov_id)

        for item in container.query_items(query=q,enable_cross_partition_query=True):
            return item

    def get_claim_details_insurer(claim_id, ins_id):
        
        q='SELECT * FROM mycontainer r WHERE r.ClaimID="{}" AND r. InsCode="{}"'.format(claim_id, ins_id)

        for item in container.query_items(query=q,enable_cross_partition_query=True):
            return item

    def get_claim_status_insurer(claim_id, ins_id):
        q= 'SELECT * FROM mycontainer r WHERE r.ClaimID="{}" AND r.InsCode = "{}"'.format(claim_id, ins_id)
        for item in container.query_items (query=q,enable_cross_partition_query=True):
            return item

    def get_claim_status_provider (claim_id,prov_id):
        q= 'SELECT * FROM mycontainer r WHERE r.ClaimID="{}" AND r.ProvCode="{}"'.format(claim_id,prov_id) 
        for item in container.query_items (query=q,enable_cross_partition_query=True):
            return item

    def get_provider(prov_id):
        q= 'SELECT * FROM mycontainer r WHERE r.ProvCode = "{}"'.format(prov_id)
        for item in container.query_items (query=q,enable_cross_partition_query=True):
            return item

    def get_insurer(ins_id):
        q= 'SELECT * FROM mycontainer r WHERE r.InsCode = "{}"'.format(ins_id)
        for item in container.query_items (query=q,enable_cross_partition_query=True):
            return item