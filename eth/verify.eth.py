#!/usr/bin/env python
# import ethereum
from ethereum.utils import sha3,normalize_key
from ethereum.utils import privtoaddr,privtopub
from ethereum.utils import ecsign,ecrecover_to_pub
from rlp.utils import decode_hex,encode_hex

def ecrecover(rawhash,v,r,s):
    pubkey = ecrecover_to_pub(rawhash,v,r,s)

from ethereum.abi import method_id
def getMethodId(funcname,params):
    code=hex(method_id(funcname,params))
    return code[:2]+'0'*(10-len(code))+code[2:]
funcid=getMethodId('allocate',['uint256','bytes32','bytes32','bytes32'])
namount=10000
hexstr=hex(namount)[2:]
hamount = '0'*(64-len(hexstr))+hexstr

# https://ethereum.stackexchange.com/questions/72941/ecrecover-always-returns-0x0000000000000000000000000000000000000000
# https://docs.soliditylang.org/en/v0.5.3/abi-spec.html#non-standard-packed-mode
# https://ethereum.stackexchange.com/questions/2171/how-does-one-properly-use-ecrecover-to-verify-ethereum-signatures

print(getMethodId('testDice',['uint256','uint256','bytes32','bytes32']))
print("case1:  56084aab0000000000000000000000000000000000000000000000000000000000b72ea2c4cbe3bb4c5adcb6e5d8b73ca4101ae4bae4f7a7c174cc95cc07dcfbd6b9e6cc9bacce7139cb65d09e4e482b50617b75f8e08e8adafffdc4d9e6ead44c89dede0c2406fbacb62b1c571c5fd8d4e6ed04bd03be2e0f6a5901899d631138ffb5f2")
print("case2:  56084aab0000000000000000000000000000000000000000000000000000000000b73b0463aa73889f0615a32095bd25b385534db729d612d6707a38fa8b98660dc2f9d3dd889d487e87a54e3bb99d402da27a0da4708b4c0caf614e05e49656d7ee546a2762b984c8cc832a6a9a4089edf2d39c7ffe2cf0aad3ff999be5d221d993494b")
print("signer: b00b5ca7ec0502f2f269e99b91ebbccbce9cccec")

print(getMethodId('testRaw',['bytes32','bytes32','bytes32']))
print("case1: 4408ea47375ef142e941b1748bd925e55d463ebdfcd7ca46105898cfb84fd2960527a6f53cf93675c89f550e3a796678c1a1d4fe8c059ca564359e6bdd579de957141f8e0e224f341a72e33ae83cf4d5823e6a763244f3a27e4ab4d225b6b62e9163025e")