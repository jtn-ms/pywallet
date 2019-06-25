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
        print int(balance,16)
        return balance
    except Exception as e: return 0
    
if __name__ == "__main__":
    getbalance("0xc94770007dda54cF92009BFF0dE90c06F603a09f")