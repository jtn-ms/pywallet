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
data = "this is the message to be encrypted"

from sha3 import keccak_256
rawhash = keccak_256(data).digest()
# rawhash = sha3(data)
print("rawhash: {0}".format(rawhash.encode('hex')))
v, r, s = ecsign(rawhash, normalize_key(privkey))
p_r = hex(r).strip("L").strip("0x")
p_s = hex(s).strip("L").strip("0x")
p_h = rawhash.encode('hex')
x_r = '0'*(64-len(p_r))+p_r
x_s = '0'*(64-len(p_s))+p_s
x_h = '0'*(64-len(p_h))+p_h
print("v: {0}, r: {1}, s: {2}".format(v,x_r,x_s))

def ecrecover(rawhash,v,r,s):
    pubkey = ecrecover_to_pub(rawhash,v,r,s)

    # print("pubkey: {0}-{1}".format(pubkey,type(pubkey)))
    return keccak_256(pubkey).digest()[-20:]
signer = ecrecover(rawhash,v,r,s)
print("signer: {0}".format(signer.encode('hex')))
assert signer == signedaddr

from ethereum.abi import method_id
def getMethodId(funcname,params):
    code=hex(method_id(funcname,params))
    return code[:2]+'0'*(10-len(code))+code[2:]
funcid=getMethodId('allocate',['uint256','bytes32','bytes32','bytes32'])
namount=10000
hexstr=hex(namount)[2:]
hamount = '0'*(64-len(hexstr))+hexstr
hexstr=hex(v)[2:]
hv = '0'*(2-len(hexstr))+hexstr
print("allocate('uint256','bytes32','bytes32','bytes32'): ")
print("{0}{1}{2}{3}".format(funcid[2:],hamount,x_h,x_r,x_s))

print("############# encode, decode testing###############")
print(type(r),r)
print(type(s),s)
print(type(rawhash),rawhash)
_r = long(hex(r).strip("L").strip("0x"),16)
_s = long(hex(s).strip("L").strip("0x"),16)
_rawhash = rawhash.encode('hex').decode("hex")

assert _r == r
assert _s == s
assert _rawhash == rawhash

# dice2.win.sol
# Function: placeBet(uint256 betMask, uint256 modulo, uint256 commitLastBlock, uint256 commit, bytes32 r, bytes32 s)

# MethodID: 0x5e83b463
# [0]:  0000000000000000000000000000000000000000000000000000000000000038
# [1]:  0000000000000000000000000000000000000000000000000000000000000006
# [2]:  0000000000000000000000000000000000000000000000000000000000b72503
# [3]:  8a68b68093f41d77e17c341a9a8a79585f5ce7ced41d1dcbe5f5f770476d7fdd
# [4]:  e6118f75e7c18033d019e3f5490f9be37d2becd82eb643eaf7fe10c7fd27fa4f
# [5]:  057089906b666936a8be0d52c5558e7c83cbe5f27fbca4a21531dc38ea7ca24a
######################
# // Check that commit is valid - it has not expired and its signature is valid.
# require (block.number <= commitLastBlock, "Commit has expired.");
# bytes32 signatureHash = keccak256(abi.encodePacked(uint40(commitLastBlock), commit));
# require (secretSigner == ecrecover(signatureHash, 27, r, s), "ECDSA signature is not valid.");
commitLastBlock = "0000000000000000000000000000000000000000000000000000000000b7270d"
commit = "e021e8dd8ae038b0414a80100de5048f2996b9fd247d0cdb1fe480c567edfb6f"
_r = "d4af6c87392704cf891c5af466c4fb31706454e92122deee475dd0b6b0a09687"
_s = "00cef18ff00f8562ffe7ab1bc0afce0f2b757c6a3c360fe8c03b9dd6be62e93e"

nblkid = int(commitLastBlock.strip("0"),16)
print("nblkid: {0}".format(nblkid))
import hashlib
import binascii
from ethereum.abi import encode_single,encode_abi
from sha3 import keccak_256
# from eth_hash.auto import keccak
print("#################### ecrecover testing(based on dice2.win's tx data)#####################")
encoded = encode_abi(('uint40','uint256'),(long(commitLastBlock,16),long(commit,16)))
print("encoded: {0}-{1}".format(encoded.encode('hex'),type(encoded)))
_rawhash=keccak_256(encoded).digest()
# print("_rawhash: {0}-{1}-{2}".format(_rawhash,type(_rawhash),len(_rawhash)))
_rawhashstr=hashlib.sha256(encoded).hexdigest()
print("_rawhashstr: {0}".format(_rawhashstr))
print("_rawhash: {0}".format(_rawhash.encode('hex')))
signer = ecrecover(_rawhash,v,long(_r,16),long(_s,16))
print("signer: {0}".format(signer.encode('hex')))
#signer: 5483fca3be2a62c2cbb581e2816837a7081d8bc1

# https://ethereum.stackexchange.com/questions/72941/ecrecover-always-returns-0x0000000000000000000000000000000000000000
# https://docs.soliditylang.org/en/v0.5.3/abi-spec.html#non-standard-packed-mode
# https://ethereum.stackexchange.com/questions/2171/how-does-one-properly-use-ecrecover-to-verify-ethereum-signatures

print(getMethodId('testDice',['uint256','uint256','bytes32','bytes32']))
print("case1:  56084aab0000000000000000000000000000000000000000000000000000000000b72ea2c4cbe3bb4c5adcb6e5d8b73ca4101ae4bae4f7a7c174cc95cc07dcfbd6b9e6cc9bacce7139cb65d09e4e482b50617b75f8e08e8adafffdc4d9e6ead44c89dede0c2406fbacb62b1c571c5fd8d4e6ed04bd03be2e0f6a5901899d631138ffb5f2")
print("case2:  56084aab0000000000000000000000000000000000000000000000000000000000b73b0463aa73889f0615a32095bd25b385534db729d612d6707a38fa8b98660dc2f9d3dd889d487e87a54e3bb99d402da27a0da4708b4c0caf614e05e49656d7ee546a2762b984c8cc832a6a9a4089edf2d39c7ffe2cf0aad3ff999be5d221d993494b")
print("signer: b00b5ca7ec0502f2f269e99b91ebbccbce9cccec")

print(getMethodId('testRaw',['bytes32','bytes32','bytes32']))
print("case1: 4408ea47375ef142e941b1748bd925e55d463ebdfcd7ca46105898cfb84fd2960527a6f53cf93675c89f550e3a796678c1a1d4fe8c059ca564359e6bdd579de957141f8e0e224f341a72e33ae83cf4d5823e6a763244f3a27e4ab4d225b6b62e9163025e")