#!/usr/bin/env python3

# var sig = secp256k1.sign(msgHash, privateKey)
# var ret = {}
# ret.r = sig.signature.slice(0, 32)
# ret.s = sig.signature.slice(32, 64)
# ret.v = sig.recovery + 27

# from ethereum.utils import sha3
import json

import web3
import web3.eth
from web3 import Web3, HTTPProvider
from web3.contract import Contract

signed_url = "https://mainnet.infura.io/v3/09af14756ba347898112f3b8259e9e6e"
w3 = Web3(HTTPProvider(signed_url))


addr = "0xc6f4f527587ea4a03aa85e0322783592367c1b9a"
ethaddr = Web3.toChecksumAddress(addr[2:] if '0x' in addr else addr)
# Web3.sha3(0x747874)
# Web3.sha3(b'\x74\x78\x74')
# Web3.sha3(hexstr='0x747874')
# Web3.sha3(hexstr='747874')
# Web3.sha3(text='txt')
encoded = '0x70617373776f7264'
privkey = w3.sha3(hexstr=ethaddr)
print(privkey.hex(),type(privkey))

import web3

# Eth.sign(account, data=None, hexstr=None, text=None)
##########
# Examples
##########
# web3.eth.sign(
#       '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
#       text='some-text-tö-sign')
# '0x1a8bbe6eab8c72a219385681efefe565afd3accee35f516f8edf5ae82208fbd45a58f9f9116d8d88ba40fcd29076d6eada7027a3b412a9db55a0164547810cc401'

# web3.eth.sign(
#       '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
#       data=b'some-text-t\xc3\xb6-sign')
# '0x1a8bbe6eab8c72a219385681efefe565afd3accee35f516f8edf5ae82208fbd45a58f9f9116d8d88ba40fcd29076d6eada7027a3b412a9db55a0164547810cc401'

# web3.eth.sign(
#       '0xd3CdA913deB6f67967B99D67aCDFa1712C293601',
#       hexstr='0x736f6d652d746578742d74c3b62d7369676e')
# '0x1a8bbe6eab8c72a219385681efefe565afd3accee35f516f8edf5ae82208fbd45a58f9f9116d8d88ba40fcd29076d6eada7027a3b412a9db55a0164547810cc401'
sig = w3.eth.sign(ethaddr, text=privkey.hex())
print(type(sig))