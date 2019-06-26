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

def str2dict(string):
    json_acceptable_string = string.replace("'", "\"")
    return json.loads(json_acceptable_string)

def getbalance(address):
    address = "0x%s"%address if not address.startswith("0x") else address
    try:
        url = 'https://api.infura.io/v1/jsonrpc/mainnet/eth_getBalance?params=%5B%22{0}%22%2C%22latest%22%5D'.format(address)
        # print address
        res = requests.get(url)
        if res.status_code != 200:
            return 0
        balance = str2dict(res.text)["result"]
        return int(balance,16)/float(10**18)
    except Exception as e: return 0

def getnonce(address):
    address = "0x%s"%address if not address.startswith("0x") else address
    try:
        url = 'https://api.infura.io/v1/jsonrpc/mainnet/eth_getTransactionCount?params=%5B%22{0}%22%2C%22latest%22%5D'.format(address)
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
        url = 'https://api.infura.io/v1/jsonrpc/mainnet'
        params = {
                    "id": 1337,
                    "jsonrpc": "2.0",
                    "method": "eth_sendRawTransaction",
                    "params": [signed]
                }
        cmd = "curl -sX POST --data '{0}' {1}".format(str(params).replace("'", '"'),url)
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