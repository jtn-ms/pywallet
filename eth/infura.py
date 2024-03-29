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



try:
    from eth.setting import INFURA_SIGNED_URL
    from eth.utils import str2dict, extractResult
except:
    from .utils import str2dict, extractResult
    from .setting import INFURA_SIGNED_URL

signed_url = INFURA_SIGNED_URL

def rpc_call(params):
    if isinstance(params,dict):
        params = str(params).replace("'", '"')
    cmd = "curl --silent -i -X POST -H 'Content-Type: application/json' --data '{0}' {1}".format(params,signed_url)
    # print address
    import subprocess
    return subprocess.getoutput(cmd).split("\n")[-1]

# ('HTTP/1.1 200 OK\r\nDate: Tue, 02 Mar 2021 10:10:34 GMT\r\nContent-Type: application/json\r\nContent-Length: 54\r\nConnection: keep-alive\r\nVary: Origin\r\n\r\n{"jsonrpc":"2.0","id":1,"result":"0x773da15214bb8c00"}', <type 'str'>)
# https://medium.com/@piyopiyo/how-to-get-ethereum-balance-with-json-rpc-api-provided-by-infura-io-6e5d22d25927
def getBalance(address):
    address = "0x%s"%address if not address.startswith("0x") else address
    try:
        params = { "jsonrpc":"2.0",
                   "method":"eth_getBalance",
                   "params":[address,"latest"],
                   "id":1}
        
        res = rpc_call(params)
        if "result" not in res:
            return res
        balance = extractResult(res)
        return int(balance,16)/float(10**18)
    except Exception as e: return 0

def callContract(contractaddr,data):
    contractaddr = "0x%s"%contractaddr if not contractaddr.startswith("0x") else contractaddr
    try:
        params = { "jsonrpc":"2.0",
                   "method":"eth_call",
                   "params":[{'to':contractaddr,'data': data}, "latest"],
                   "id":1}
        
        res = rpc_call(params)
        if "result" not in res:
            return res
        balance = extractResult(res)
        return int(balance,16)/float(10**18)
    except Exception as e: return 0


def getblock(blknum):
    blknum = hex(blknum) if isinstance(blknum,int) else blknum
    blknum = "0x%s"%blknum if not blknum.startswith("0x") \
                              and blknum != "latest" else blknum
    if blknum != "latest":
        try:
            int(blknum,16)
        except Exception as e: return ''
    try:
        params = '{ "jsonrpc":"2.0", \
                    "method":"eth_getBlockByNumber", \
                    "params":["%s",false],\
                    "id":1}'%blknum
        params=params.replace(" ",'')
        res = rpc_call(params)
        if "result" not in res:
            return ''
        result = extractResult(res,skey='"result":',ekey='}')+"}"
        print(result,type(result))
        return str2dict(result)
    except Exception as e: print(e);return ''

def getblockHashByNumber(blknum):
    blkres = getblock(blknum)
    if blkres == '':
        return ''
    import sys
    if sys.version_info[0]<3:
        blknum = blkres[unicode('number')].encode('ascii','ignore')
        blkhash = blkres[unicode('hash')].encode('ascii','ignore')
    else: 
        blknum,blkhash = blkres['number'],blkres['hash']
    return int(blknum,16),blkhash

def getnonce(address):
    address = "0x%s"%address if not address.startswith("0x") else address
    try:
        params = { "jsonrpc":"2.0",
                   "method":"eth_getTransactionCount",
                   "params":[address,"latest"],
                   "id":1}
        
        res = rpc_call(params)
        if "result" not in res:
            return 0
        nonce = extractResult(res)
        return int(nonce,16)
    except Exception as e: return 0

def sendrawtransaction(signed):
    signed = "0x%s"%signed if not signed.startswith("0x") else signed
    try:
        params = {
                    "id": 1,
                    "jsonrpc": "2.0",
                    "method": "eth_sendRawTransaction",
                    "params": [signed]
                }
        
        res = rpc_call(params)
        if "result" not in res:
            return extractResult(res)
        return extractResult(res,'"message":"')
    except Exception as e: return ""

if __name__ == "__main__":
    # print(getblockHashByNumber("latest"))
    # print(getBalance("0xddfd7f68662bef333bb7891580948e83dcd3c988"))
    print(getnonce("0xddfd7f68662bef333bb7891580948e83dcd3c988"))
    # print(callContract("0xc02aaa39b223fe8d0a0e5c4f27ead9083c756cc2",\
    #                    "0x3e5beab9000000000000000000000000ddfd7f68662bef333bb7891580948e83dcd3c988"))