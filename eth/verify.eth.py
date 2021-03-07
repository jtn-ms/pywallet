#!/usr/bin/env python
import ethereum
from ethereum.utils import sha3,normalize_key
from ethereum.utils import privtoaddr,privtopub
from ethereum.utils import ecsign,ecrecover_to_pub
from rlp.utils import decode_hex,encode_hex

privkey = sha3("test")
print("privkey: {0}".format(privkey.encode('hex')))
signedaddr = privtoaddr(privkey)
print("signedaddr: {0}".format(signedaddr.encode('hex')))
# data = sha3("this is the message to be encrypted").encode('hex')
# rlpdata = decode_hex(data[2:]) if isinstance(data,str) and data.startswith('0x') else decode_hex(data)
# print(rlpdata)
# rawhash = sha3(rlpdata)
rawhash = sha3("this is the message")
print("rawhash: {0}".format(rawhash.encode('hex')))
v, r, s = ecsign(rawhash, normalize_key(privkey))
print("v: {0}, r: {1}, s: {2}".format(v,hex(r).strip("L"),hex(s).strip("L")))
pubkey = ecrecover_to_pub(rawhash,v,r,s)
from sha3 import keccak_256
signer = keccak_256(pubkey).digest()[-20:]
print("signer: {0}".format(signer.encode('hex')))
assert signer == signedaddr
# from eth_keys import keys
# from eth_utils import decode_hex
# priv_key = keys.PrivateKey(privkey)
# pub_key = priv_key.public_key
# print(priv_key,pub_key)