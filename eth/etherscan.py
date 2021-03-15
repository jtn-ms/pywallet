#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://etherscan.io/apis
import requests

API_KEY = "CVUQPN89HJIF5PJ3T2UZMNE3NH5GGCZIKY"

from req_util import str2dict,extractResult

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
        print(res.text)
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

if __name__ == "__main__":
    # getBalance("0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae")
    # getBlock("latest")
    print(getBlockHash("latest"))