#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://etherscan.io/apis
import requests

try:
    from eth.consts import ETHERSCAN_KEY as API_KEY
    from eth.req_util import str2dict,extractResult
except:
    from req_util import str2dict,extractResult
    from consts import ETHERSCAN_KEY as API_KEY

def getBalance(address):
    address = "0x%s"%address if not address.startswith("0x") else address
    url = "https://api.etherscan.io/api?\
           module=account&\
           action=balance&\
           address={0}&\
           tag=latest&\
           apikey={1}".format(address,API_KEY)
    url = url.replace(" ","")
    try:
        res = requests.get(url)
        if res.status_code != 200:
            return 0
        balance = str2dict(res.text)["result"]
        return int(balance)
    except Exception as e: return 0

def getBlock(blknum):
    blknum = hex(blknum) if isinstance(blknum,int) else blknum
    blknum = "0x%s"%blknum if not blknum.startswith("0x") \
                              and blknum != "latest" else blknum
    if blknum != "latest":
        try:
            int(blknum,16)
        except Exception as e: return ''
    url = "https://api.etherscan.io/api?\
           module=proxy&\
           action=eth_getBlockByNumber&\
           tag={0}&\
           boolean=true&\
           apikey={1}".format(blknum,API_KEY)
    url = url.replace(" ","")
    try:
        res = requests.get(url)
        if res.status_code != 200:
            return ''
        return str2dict(res.text)[unicode('result')]
    except Exception as e: return ''

def getBlockHash(blkum):
    blkres = getBlock(blkum)
    if blkres == '':
        return -1,""
    blknum = blkres[unicode('number')].encode('ascii','ignore')
    blkhash = blkres[unicode('hash')].encode('ascii','ignore')
    return int(blknum,16),blkhash

def getTokenBalance(contractaddr,address):
    contractaddr = "0x%s"%contractaddr if not contractaddr.startswith("0x") else contractaddr
    address = "0x%s"%address if not address.startswith("0x") else address
    url = "https://api.etherscan.io/api?module=account&action=tokenbalance&\
           contractaddress={0}&\
           address={1}&\
           tag=latest&\
           apikey={2}".format(contractaddr,address,API_KEY)
    url = url.replace(" ","")
    print(url)
    try:
        res = requests.get(url)
        if res.status_code != 200:
            return 0
        # print(res.text)
        balance = str2dict(res.text)["result"]
        return int(balance)
    except Exception as e: return 0

# https://etherscan.io/token/0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2    
if __name__ == "__main__":
    # print(getBalance("0000000000000000000000000000000000000000"))
    # getBlock("latest")
    # print(getBlockHash("latest"))
    print(getTokenBalance("0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",\
                          "8e44115bcc1bbc395eee326331c2ee38e0e1b1e2"))