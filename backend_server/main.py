import os
from ocean_lib.config import Config
from web3 import Web3
from ocean_lib.config_provider import ConfigProvider
from ocean_lib.web3_internal.wallet import Wallet
from ocean_lib.ocean.util import get_web3_connection_provider
from ocean_lib.web3_internal.web3_provider import Web3Provider
from ocean_lib.web3_internal.contract_handler import ContractHandler
from ocean_lib.ocean.ocean import Ocean
from dotenv import load_dotenv
from ocean_lib.ocean.ocean import Ocean
from ocean_lib.web3_internal.wallet import Wallet
from trying import trying_compute

def initialize(private_key):
    load_dotenv(".env")
    config = Config(os.getenv('config.ini'))
    config = Config(os.getenv('config.ini'))
    print(config.network_url)
    # config.network_url="https://rinkeby.infura.io/v3/31d95be121a545b688a0e07e4de4d256"
    ConfigProvider.set_config(config)
    Web3Provider.init_web3(provider=get_web3_connection_provider(config.network_url))
    ContractHandler.set_artifacts_path(config.artifacts_path)
    ocean=Ocean()
    wallet = Wallet(ocean.web3, private_key=private_key)
    return ocean,wallet
#
# date_created = "2021-03-01T10:55:11Z"
# service_attributes = {
#         "main": {
#             "name": "dataAssetAccessServiceAgreement",
#             "creator": s
#             "timeout": 3600 * 24,
#             "datePublished": date_created,
#             "cost": 10.0, # <don't change, this is obsolete>
#         }
#     }

def create_token(name1,name2,wallet,ocean):
    print("here")
    data_token = ocean.create_data_token(name1, name2, wallet, blob=ocean.config.metadata_store_url)
    token_address = data_token.address
    return data_token,token_address


from ocean_lib.data_provider.data_service_provider import DataServiceProvider
from ocean_utils.agreements.service_factory import ServiceDescriptor
date_created = "2012-02-01T10:55:11Z"
metadata =  {
    "main": {
        "type": "dataset", "name": "10 Monkey Species Small", "author": "Mario",
        "license": "CC0: Public Domain", "dateCreated": date_created,
        "files": [
            { "index": 0, "contentType": "application/zip", "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/assets/training.zip"},
            { "index": 1, "contentType": "text/text", "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/assets/monkey_labels.txt"},
            { "index": 2, "contentType": "application/zip", "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/assets/validation.zip"}]}
}




def create_asset(ocean,wallet,service_attributes,metadata,token_address):

    service_endpoint = DataServiceProvider.get_url(ocean.config)
    download_service = ServiceDescriptor.access_service_descriptor(service_attributes, service_endpoint)
    compute_attributes=trying_compute(wallet)
    computer_service=ServiceDescriptor.compute_service_descriptor(compute_attributes,service_endpoint)
    print(download_service)
    print(computer_service)
    print("kjashdfkhaskdfhkjhasdjkfhkjasdhfjkasdhjkfhajkdshf")
    asset = ocean.assets.create(metadata, wallet, service_descriptors=[download_service], data_token_address=token_address)
    return asset

def makepool(ocean,wallet,token_address):
    pool=ocean.pool.create(
        token_address,
        data_token_amount=100,
        OCEAN_amount=1,
        from_wallet=wallet
    )
    return pool.address

def return_asest(did):
    asset=market_ocean.assets.resolve(did)
    return asset


#
# pool = ocean.pool.create(
#    token_address,
#    data_token_amount=10,
#    OCEAN_amount=5,
#    from_wallet=wallet
# )
#
#
# pool_address = pool.address
# print(f'DataToken @{data_token.address} has a `pool` available @{pool_address}')
# import pickle as p
# d
# with open("object.dump",'w') as f:
#     p.dump(d,f)