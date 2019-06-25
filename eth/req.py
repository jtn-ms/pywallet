# -*- coding: utf-8 -*-
# https://api.infura.io/v1/jsonrpc/mainnet/eth_getBalance?params=%5B%220xc94770007dda54cF92009BFF0dE90c06F603a09f%22%2C%22latest%22%5D
# %5B: [
# %22: "
# %2C: ,
# %5D: ]

import requests
import json

def str2dict(string):
    json_acceptable_string = string.replace("'", "\"")
    return json.loads(json_acceptable_string)

def getbalance(address):
    try:
        url = 'https://api.infura.io/v1/jsonrpc/mainnet/eth_getBalance?params=%5B%22{0}%22%2C%22latest%22%5D'.format(address)
        print address
        res = requests.get(url)
        if res.status_code != 200:
            return 0
        balance = str2dict(res.text)["result"]
        return int(balance,16)/float(10**18)
    except Exception as e: return 0

# from wallets such as metamask, imtoken
# metamask: https://metamask.github.io/metamask-docs/API_Reference/JSON_RPC_API
#           http://api.infura.io/v1/jsonrpc/main/eth_sendRawTransaction?params=%5B%220xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675%22%2Ctrue%5D
# & etherscan apis
# eth_sendRawTransaction: https://api.etherscan.io/api?module=proxy&action=eth_sendRawTransaction&hex=0xf904808000831cfde080&apikey=YourApiKeyToken
# 
def sendrawtransaction(signed):
    try:
        url = 'http://api.infura.io/v1/jsonrpc/main/eth_sendRawTransaction?params=%5B%22{0}%22%2Ctrue%5D'.format(signed)
        res = requests.post(url)
        if res.status_code != 200:
            return False
        return True
    except Exception as e: return False

if __name__ == "__main__":
    print getbalance("0xc94770007dda54cF92009BFF0dE90c06F603a09f")