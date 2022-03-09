#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://etherscan.io/apis
import requests
import sys

try:
    from eth.setting import ETHERSCAN_KEY as API_KEY
    from eth.setting import ETHERSCAN_API_URL as API_URL
    from eth.utils import str2dict,extractResult,getResponse
except:
    from .setting import ETHERSCAN_KEY as API_KEY
    from .setting import ETHERSCAN_API_URL as API_URL
    from .utils import str2dict,extractResult,getResponse

def getBalance(address) -> int:
    address = "0x%s"%address if not address.startswith("0x") else address
    url = "{0}/api?\
           module=account&\
           action=balance&\
           address={1}&\
           tag=latest&\
           apikey={2}".format(API_URL,address,API_KEY)
    url = url.replace(" ","")
    result = getResponse(url)
    result = 0 if not result else int(result)
    return result

def getBlock(blknum) -> str:
    blknum = hex(blknum) if isinstance(blknum,int) else blknum
    blknum = "0x%s"%blknum if not blknum.startswith("0x") \
                              and blknum != "latest" else blknum
    if blknum != "latest":
        try:
            int(blknum,16)
        except Exception as e: return ''
    url = "{0}/api?\
           module=proxy&\
           action=eth_getBlockByNumber&\
           tag={1}&\
           boolean=true&\
           apikey={2}".format(API_URL,blknum,API_KEY)
    url = url.replace(" ","")
    result = getResponse(url)
    return result

def getBlockHash(blkum):
    blkres = getBlock(blkum)
    if blkres == '':
        return -1,""
    if sys.version_info[0]<3:
        blknum = blkres[unicode('number')].encode('ascii','ignore')
        blkhash = blkres[unicode('hash')].encode('ascii','ignore')
    else: 
        blknum = blkres['number']#.encode('ascii','ignore')
        blkhash = blkres['hash']#.encode('ascii','ignore')   
    return int(blknum,16),blkhash

def getTokenBalance(contractaddr,address)->int:
    contractaddr = "0x%s"%contractaddr if not contractaddr.startswith("0x") else contractaddr
    address = "0x%s"%address if not address.startswith("0x") else address
    url = "{0}/api?module=account&action=tokenbalance&\
           contractaddress={1}&\
           address={2}&\
           tag=latest&\
           apikey={3}".format(API_URL,contractaddr,address,API_KEY)
    url = url.replace(" ","")
    print(url)
    result = getResponse(url)
    result = 0 if not result else int(result)
    return result
    
if __name__ == "__main__":
    # print(getBalance("0x0000000000000000000000000000000000000000"))
    # getBlock("latest")
    print(getBlockHash("latest"))
    # print(getTokenBalance("0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",\
    #                       "a1b1ee61f7102dfdc5c374957afc402225ed1e58"))