import flask
from datetime import datetime
from flask import jsonify,request
from main import initialize,create_token,create_asset,makepool
import random
from flask import send_from_directory,send_file
from ocean_utils.agreements.service_types import ServiceTypes
import zipfile
import os
import trying
import datetime
from trying import ocean,auth_ocean_token,get_compute_back
from ocean_lib.config import Config
from web3 import Web3
from ocean_lib.config_provider import ConfigProvider
from ocean_lib.ocean.ocean_compute import  OceanCompute
from ocean_lib.ocean.ocean_auth import OceanAuth

#
app=flask.Flask(__name__)
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))



zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
zipdir('/home/aniket/PycharmProjects/doing_stuff_with_ocean/files/datafile.0xff95E418d7D6DBE825370202AE3E66A8Eb6864E6.3', zipf)
zipf.close()


# json signaturetoken_name=("".join for x in [random.choice("abcdefghizklmnopqrstyvwxyz") for _ in range(10)])
"""
{
"privatekey":
"serviceattributes":
"metadate":

}


"""
date_created = "2021-06-01T10:55:11Z"

def get_meta_data(url):
    date_published = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat() + "Z"
    metadata =  {
        "main": {
            "type": "dataset", "name": "niceitsworking", "author": "Lallalalala",
            "license": "CC0: Public Domain", "dateCreated": date_published,
            "files": [
                { "index": 0, "contentType": "text/json", "url": f"{url}"}]}}
    return metadata


def return_service_attribute(address):
    service_attributes = {
            "main": {
                "name": "dataAssetAccessServiceAgreement",
                "creator": address,
                "timeout": 3600 * 24,
                "datePublished": date_created,
                "cost": 1 # <don't change, this is obsolete>
            }
        }
    return service_attributes

@app.route("/",methods=["GET"])
def home():
    return {"message":"ok"},200

@app.route("/datatoken",methods=["GET","POST"])
def datatoken():
    """
    :param:private_key of the publisher
    :return:token_name,token_address,token_hash
    """
    try:
        content=request.get_json()
        print(content["privatekey"])
        ocean,wallet=initialize(content["privatekey"])
        # service_attributes=return_service_attribute(wallet)
        print(wallet.address)
        # print(service_attributes)
        token_name=[random.choice("abcdefghizklmnopqrstyvwxyz") for _ in range(10)]
        name1="DataToken"+str(random.randint(0,1000000))
        token_name="".join(x for x in token_name)
        print(token_name,name1)

        data_token,token_address=create_token(name1,token_name,wallet,ocean)
        mint_hash=data_token.mint_tokens(wallet.address,1000,wallet)

        return {"token_name":token_name,"token_hash":mint_hash,"token_address":token_address},200
    except Exception as e:
        return {"message":"error"},404

@app.route("/publish",methods=["POST"])
def publish():
    """
    :param:privatekkey, token,url for the file
    :return: did for the published asset
    """
    content=request.get_json()
    token_address=content["token"]
    ocean,wallet=initialize(content["privatekey"])
    print(wallet.address)
    s=return_service_attribute(wallet.address)
    url=content["url"]
    metadata=get_meta_data(url)
    asset=create_asset(ocean=ocean,wallet=wallet,metadata=metadata,service_attributes=s,token_address=token_address)
    # print(asset)
    return {"token":token_address,"did":asset.did}
    # return {"message":"aaa"}

@app.route("/pool",methods=["POST"])
def make_pool():
    """
    :param : private_key,token_address
    :return: retursn the token address and the pool address
    """
    if request.is_json:
        content=request.get_json()
        private_key=content["privatekey"]
        token_address=content["token"]
        # data_amount=content["data_amount"]
        # ocean_amount=content["ocean_amount"]

        ocean,wallet=initialize(private_key=private_key)
        pool_address=makepool(ocean,wallet,token_address)
        return {
            "token_address":token_address,
            "pool_address":pool_address
        },200
    else:
        return {},404

@app.route("/buy",methods=["POST"])
def ocean_price():
    """
    :param:privatekey,pool address, did
    :return:token prize in comparision to the ocean token
    """
    if request.is_json:
        # a buy parameter which will tell the ocean to but the shit or not ? true or false
        content=request.get_json()
        # private key here will be the consumers private key and not the publishers private key
        private_key=content["privatekey"]
        did=content["did"]
        token_address=content["token"]

        pool_address=content["pool_address"]
        ocean,wallet=initialize(private_key)
        data_token = ocean.get_data_token(token_address)
        # asset=ocean.assets.resolve(did)
        # print(asset.did)
        # service=asset.get_service(ServiceTypes.ASSET_ACCESS)
        OCEAN_address = "0x8967BCF84170c91B0d24D4302C2376283b0B3a07"
        # OCEAN_address=ocean.pool.ocean_address
        # print(OCEAN_address)
        # price_in_ocean=ocean.pool.calcInGivenOut(
        #     pool_address,OCEAN_address,token_address,token_out_amount=1.0
        # )
        # print(price_in_ocean)
        # if content["buy"]=="false":
        #     return {"pool_address":pool_address,"price":price_in_ocean} ,200
        # else:
        ocean.pool.buy_data_tokens(pool_address,amount=1.0,max_OCEAN_amount=10,from_wallet=wallet)
        return {"message":"ok"},200



@app.route("/download",methods=["POST"])
def download():
    """
    :param:privatekey,did,numbers
    :return: whole dataset or the names for the requested numbers
    """
    if request.is_json:
        content=request.get_json()
        if content["service"]=="download":
            privatekey=content["privatekey"]
            ocean,wallet=initialize(privatekey)
            did=content["did"]
            asset=ocean.assets.resolve(did)
            service=asset.get_service(ServiceTypes.ASSET_ACCESS)
            print(service)
            quote=ocean.assets.order(asset.did,wallet.address,service_index=service.index)
            # putting the buy option here
            token_address=quote.data_token_address
            print(token_address)

            # OCEAN_address = ocean.pool.ocean_address
            # pool_address = content["pool_address"]
            # price_in_ocean = ocean.pool.calcInGivenOut(
            #     pool_address, OCEAN_address, token_address, token_out_amount=1.0
            # )
            # print(price_in_ocean)
            # data_token = ocean.pool.buy_data_tokens(pool_address, amount=1.0, max_OCEAN_amount=price_in_ocean,
            #                               from_wallet=wallet)
            # print(data_token)
            market_address="0x8967BCF84170c91B0d24D4302C2376283b0B3a07"
            order_tx_id = ocean.assets.pay_for_service(
                quote.amount, quote.data_token_address, asset.did, service.index, market_address, wallet
            )
            print(order_tx_id)
            filepath=ocean.assets.download(
                asset.did,
                service.index,
                wallet,
                order_tx_id,
                destination="./files"
            )
            if "numbers" not in content.keys():
                zip_filename="data"+token_address+".zip"
                zipf = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)
                zipdir(filepath,zipf)
                zipf.close()

                send_file(zip_filename)
                return {"message":"ok","order_txn":order_tx_id},200
            else:
                numbers=content["numbers"]
                return_data=get_compute_back(did[7:],numbers)
                if len(return_data.keys())==0:
                    return_data["message"]="data not found"
                    return return_data,404
                return_data["message"]="data found"
                return return_data,200






@app.route("/compute",methods=["POST"])
def compute():
    """
    :param:in development correspoding to the ocean protocol
    :return:
    """
    if request.is_json:
        content=request.get_json()
        did=content["did"]
        privatekey=content["privatekey"]
        ocean,wallet=initialize(privatekey)
        order_tx_id=content["order_txn"]
        nonce =10000
        job_id=trying.trying_algorithm_run(did,wallet,order_tx_id,nonce)
        return {"job_id":job_id},200






if __name__=="__main__":
    app.run(host="0.0.0.0",port="5001",debug=True)
