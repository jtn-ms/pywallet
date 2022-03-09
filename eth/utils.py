# -*- coding: utf-8 -*-
#!/usr/bin/env python
import json
import os
def str2dict(string):
    json_acceptable_string = string.replace("'", "\"").replace("\n","")
    return json.loads(json_acceptable_string)

import sys
def hexstr2int(hexstr)->int:
    if sys.version_info[0]<3:
        return long(hexstr.strip("L").strip("0x"),16)
    else: 
        return int(hexstr,16) if "0x"  not in hexstr else int(hexstr,0)

def hexstr2bytes(hexstr):
    if sys.version_info[0]<3:
        return hexstr.decode("hex")
    else: 
        return bytes.fromhex(hexstr)

def bytes2hexstr(b)->str:
    if sys.version_info[0]<3:
        return b.encode("hex")
    else: 
        return bytes.fromhex(b)    



import requests
def getResponse(url):
    return getResult(url)
    try:
        res = requests.get(url)
        if res.status_code != 200:
            return ''
        import sys
        if sys.version_info[0]<3:
            return str2dict(res.text)[unicode('result')]
        else: return str2dict(res.text)['result']
    except Exception as e: return ''    

import sys
# Execute shell commands.
def runscript(script):
    if sys.version_info[0]<3:
        import commands
        result = commands.getstatusoutput(script).split("\n")
    else:
        import subprocess
        result = subprocess.getoutput(script).split("\n")
    return result

def getResult(url):
    result = runscript('curl -s "%s"'%url)
    if len(result) < 1: return ''
    try:
        import json
        decoded=json.loads(result[0])
        return decoded["result"]
    except: return ''

def extractResult(content,skey='"result":"',ekey='"'):
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

if __name__ == "__main__":
    url="https://api-ropsten.etherscan.io/api?module=account&action=balance&address=0x0000000000000000000000000000000000000000&tag=latest&apikey=HBBSYKXCKVWRNYQ4A6WWCGDYFY3F3KZ8AC"
    result = getResult(url)
    print(result)
    print(type(result))