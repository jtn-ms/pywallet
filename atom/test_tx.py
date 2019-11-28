# -*- coding: utf-8 -*-
# written by junying, 2019-06-10

import hashlib
import coincurve
import base64
import requests
# import py.test

from atom.tx import accountinfo,transfer

block_time = 20

def test_tx_htdf():
    hrp='htdf'
    fromprivkey = 'c9960987611a40cac259f2c989c43a79754df356415f164ad3080fdc10731e65'
    frompubkey = '02fa63a1fc6f38936562bac0649dde139b527d37788dd466d27259753fe5e555d0'
    fromaddr = 'htdf12sc78p9nr9s8qj06e2tqfqhlwlx0ncuq8l9gsh'
    toaddr = 'htdf18rudpyaewcku05c87xzgaw4rl8z3e5s6vefu4r'
    restapi = '47.98.194.7:1317'
    chainid = 'testchain'
    ngas,nfee = 200000, 20
    nAmount = 0.001234 * (10**8)    #以satoshi为单位,    1USDP  = 10^8 satoshi    1HTDF=10^8 satoshi
    from atom.key import privkey2addr
    assert (frompubkey,fromaddr) == privkey2addr(fromprivkey,hrp)
    tic=accountinfo(fromaddr)
    transfer(hrp,fromprivkey, toaddr, nAmount, chainid, nfee, ngas,restapi)
    import time
    time.sleep(block_time)
    assert tic != accountinfo(fromaddr)
    