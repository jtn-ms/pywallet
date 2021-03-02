# -*- coding: utf-8 -*-
# from wallets such as metamask, imtoken
# 1. metamask: https://metamask.github.io/metamask-docs/API_Reference/JSON_RPC_API
# https://api.infura.io/v1/jsonrpc/mainnet/eth_getBalance?params=%5B%220xc94770007dda54cF92009BFF0dE90c06F603a09f%22%2C%22latest%22%5D
# %5B: [
# %22: "
# %2C: ,
# %5D: ]
# curl -X POST --data '{
#     "id": 1337,
#     "jsonrpc": "2.0",
#     "method": "eth_sendRawTransaction",
#     "params": ["0xf86b018502540be4008252089464634c470b77eea12ee17a6a4d85fef301520d468711c37937e08000801ba07e2964cd4b3b7043cb10bd121ba7e37889c084e0928844f005c3f8aa7532dec7a07ba62eeb58bc9ec796e850af40f3cf79d8df690a773547ec7760beeb4be62925"]
# }' https://api.infura.io/v1/jsonrpc/mainnet
# 2. etherscan apis
# https://etherscan.io/pushTx
# https://api.etherscan.io/api?module=proxy&action=eth_sendRawTransaction&hex=0xf904808000831cfde080&apikey=YourApiKeyToken

import requests
import json

signed_url = "https://mainnet.infura.io/v3/09af14756ba347898112f3b8259e9e6e"

def str2dict(string):
    json_acceptable_string = string.replace("'", "\"")
    return json.loads(json_acceptable_string)

skey = '"result":"'
ekey = '"'

def extractResult(content):
    sidx,eidx=-1,-1

    try:
        sidx = content.index(skey) + len(skey)
    except:
        sidx = -2

    if sidx > 0:
        try:
            eidx = content[sidx:].index(ekey)
        except:
            eidx = -2
        if eidx > 0:
            return content[sidx:sidx+eidx]
    return ""

# ('HTTP/1.1 200 OK\r\nDate: Tue, 02 Mar 2021 10:10:34 GMT\r\nContent-Type: application/json\r\nContent-Length: 54\r\nConnection: keep-alive\r\nVary: Origin\r\n\r\n{"jsonrpc":"2.0","id":1,"result":"0x773da15214bb8c00"}', <type 'str'>)
# https://medium.com/@piyopiyo/how-to-get-ethereum-balance-with-json-rpc-api-provided-by-infura-io-6e5d22d25927
def getbalance(address):
    address = "0x%s"%address if not address.startswith("0x") else address
    try:
        params = { "jsonrpc":"2.0",
                   "method":"eth_getBalance",
                   "params":[address,"latest"],
                   "id":1}
        
        cmd = "curl -i -X POST -H 'Content-Type: application/json' --data '{0}' {1}".format(str(params).replace("'", '"'),signed_url)
        # print address
        import subprocess
        res = subprocess.check_output(cmd,shell=True)
        if "result" not in res:
            return 0
        balance = extractResult(res)
        return int(balance,16)/float(10**18)
    except Exception as e: return 0

def getnonce(address):
    address = "0x%s"%address if not address.startswith("0x") else address
    try:
        url = '{0}/eth_getTransactionCount?params=%5B%22{1}%22%2C%22latest%22%5D'.format(signed_url,address)
        # print address
        res = requests.get(url)
        if res.status_code != 200:
            return 0
        nonce = str2dict(res.text)["result"]
        return int(nonce,16)
    except Exception as e: return 0
    
def sendrawtransaction(signed):
    signed = "0x%s"%signed if not signed.startswith("0x") else signed
    try:
        params = {
                    "id": 1337,
                    "jsonrpc": "2.0",
                    "method": "eth_sendRawTransaction",
                    "params": [signed]
                }
        cmd = "curl -sX POST --data '{0}' {1}".format(str(params).replace("'", '"'),signed_url)
        # res = requests.post(url,json=json.dumps(params))
        # print res.text
        # if res.status_code != 200:
        #     return False
        # return str2dict(res.text)["result"]
        import subprocess
        return subprocess.check_output(cmd,shell=True)
    except Exception as e: return False

if __name__ == "__main__":
    print getbalance("0xfac648c71eae43c518bc6676eb29ebb448d6e794")