import os
from datetime import date
from ocean_lib.ocean.ocean import Ocean
from ocean_lib.web3_internal.wallet import Wallet
from ocean_lib.data_provider.data_service_provider import DataServiceProvider
from ocean_utils.agreements.service_factory import ServiceDescriptor
import datetime
from ocean_lib.ocean.ocean_compute import  OceanCompute
from ocean_lib.ocean.ocean_auth import OceanAuth
import json

ocean = Ocean()
from dotenv import load_dotenv
# from main import initialize
#
from ocean_lib.config import Config
from web3 import Web3
from ocean_lib.config_provider import ConfigProvider
#
# alice_wallet = Wallet(ocean.web3, private_key="58ea0ec8af8f64aad99296c7e7b960ed54c94c8c49a86990a8d369ce9b9a177f")
# trying to make compute jobs in ocean protocol

# we need this auth and all for the compute job
# computer job attributes
def auth_ocean_token(wallet):
    ocean_auth=OceanAuth("./storage_tokens")
    token=ocean_auth.get(wallet)
    return ocean_auth

def get_compute_back(token,numbers=None):
    for i in os.listdir("./files"):
        if token in i:
            print("found the files")

            new_path=os.path.join("./files",i)
            try:
                f=open(os.path.join(new_path,"data.json"))
                data=json.loads(f.read())
                data=data["contacts"]
                # print(data)
                mapper={}
                final_data={}
                for number in numbers:
                    mapper[number]=None

                for name,number in data.items():
                    if number in mapper.keys():
                        final_data[number]=name
                return final_data

            except Exception as e:
                return {}

# get_compute_back("0xff95E418d7D6DBE825370202AE3E66A8Eb6864E6",["1234","2134"])

def trying_compute(wallet):
    load_dotenv(".env")
    config = Config(os.getenv('config.ini'))
    print(config.network_url)
    # config.network_url="https://rinkeby.infura.io/v3/31d95be121a545b688a0e07e4de4d256"
    ConfigProvider.set_config(config)
    ocean_auth = OceanAuth("./storage_tokens")
    token = ocean_auth.get(wallet)
    # config=ConfigProvider()
    print(config.provider_url)
    ocean_compute = OceanCompute(ocean_auth, config, config.provider_url)
    build_server_attributes = OceanCompute.build_server_attributes(server_id="1", server_type="homemade", cpu=2, gpu=0,
                                                                  memory=2, disk=10, max_run_time=5000)
    compute_service_cluster_attribute=OceanCompute.build_cluster_attributes(cluster_type="Kubernetes",url="http://10.96.0.1/")
    compute_service_container_attributes=OceanCompute.build_container_attributes(image="patanae",tag="patanae",entrypoint="python")

    compute_service_provider_attributes=OceanCompute.build_service_provider_attributes("forgeeks",description="providecompute",cluster=compute_service_cluster_attribute,containers=compute_service_container_attributes,servers=build_server_attributes)
    created_compute_service_attributes=OceanCompute.create_compute_service_attributes(creator="hello",provider_attributes=compute_service_provider_attributes,date_published="",timeout=20000)
    compute_service_descriptor=ocean_compute.create_compute_service_descriptor(created_compute_service_attributes)

algo_metadata={
    "url":"",
    "rawcode":"",
    "language":"python3.7",
    "format":"",
    "version":"1",
    "container":"",
    "container_entry_point":"python",
    "entrypoint":"somenametofill",
    "image":"",
    "tag":"somethingthat I have to do again"



}



def trying_algorithm_run(did,wallet,order_tx_id,nonce):
    load_dotenv(".env")
    config = Config(os.getenv('config.ini'))
    print(config.network_url)
    # config.network_url="https://rinkeby.infura.io/v3/31d95be121a545b688a0e07e4de4d256"
    ConfigProvider.set_config(config)
    ocean_auth = OceanAuth("./storage_tokens")
    token = ocean_auth.get(wallet)
    print(config.provider_url)
    ocean_compute=OceanCompute(ocean_auth,config,config.provider_url)

    job_id=ocean_compute.start(did,wallet,order_tx_id,nonce,algorithm_meta=algo_metadata)
    return job_id



# load_dotenv(".env")
# config = Config(os.getenv('config.ini'))
# print(config.network_url)
#     # config.network_url="https://rinkeby.infura.io/v3/31d95be121a545b688a0e07e4de4d256"
# ConfigProvider.set_config(config)
# token=ocean_auth.get(alice_wallet)
# # config=ConfigProvider()
# ocean_compute=OceanCompute(ocean_auth,config,config.provider_url)
#
# compute



#
# data_token = ocean.create_data_token('DataToken6999', 'lamaobrosthisisabot', alice_wallet, blob=ocean.config.metadata_store_url)
# token_address = data_token.address
# print(token_address,alice_wallet.address)
# date_created = "2021-06-01T10:55:11Z"
# # date_created = date.today().strftime("%Y-%m-%d")
# service_attributes = {
#         "main": {
#             "name": "dataAssetAccessServiceAgreement",
#             "creator": alice_wallet.address,
#             "timeout": 3600 * 24,
#             "datePublished": date_created,
#             "cost": 1.0, # <don't change, this is obsolete>
#         }
#     }
#
# service_endpoint = DataServiceProvider.get_url(ocean.config)
# print(service_endpoint)
#
# download_service = ServiceDescriptor.access_service_descriptor(service_attributes, service_endpoint)
# compute_service=ServiceDescriptor.compute_service_descriptor(service_attributes,service_endpoint)
# print(download_service)
# metadata =  {
#     "main": {
#         "type": "dataset", "name": "hellothisissomasdfeshit", "author": "Maasdfrio)))",
#         "license": "CC0: Public Domain", "dateCreated": date_created,
#         "files": [
#             { "index": 0, "contentType": "application/zip", "url": "https://s3.amazonaws.com/datacommons-seeding-us-east/10_Monkey_Species_Small/assets/training.zip"},]}
# }
#
# #ocean.assets.create will encrypt URLs using Provider's encrypt service endpoint, and update asset before putting on-chain.
# #It requires that token_address is a valid DataToken contract address. If that isn't provided, it will create a new token.
# asset = ocean.assets.create(metadata, alice_wallet, service_descriptors=[download_service], data_token_address=token_address)
# print(asset)
# print(asset.data_token_address)
#
# import os
# import zipfile
#
#
# def zipdir(path, ziph):
# def zipdir(path, ziph):
#     # ziph is zipfile handle
#     for root, dirs, files in os.walk(path):
#         for file in files:
#             ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))
#
#
# if __name__ == '__main__':
#     zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
#     zipdir('/home/aniket/PycharmProjects/doing_stuff_with_ocean/files/datafile.0xff95E418d7D6DBE825370202AE3E66A8Eb6864E6.3', zipf)
#     zipf.close()
