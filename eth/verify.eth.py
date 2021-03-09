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
print("v: {0}, r: {1}, s: {2}".format(v,hex(r).strip("L").strip("0x"),hex(s).strip("L").strip("0x")))

def ecrecover(rawhash,v,r,s):
    pubkey = ecrecover_to_pub(rawhash,v,r,s)

    # print("pubkey: {0}-{1}".format(pubkey,type(pubkey)))
    return keccak_256(pubkey).digest()[-20:]
signer = ecrecover(rawhash,v,r,s)
print("signer: {0}".format(signer.encode('hex')))
assert signer == signedaddr

from ethereum.abi import method_id
code=hex(method_id('allocate',['uint256','bytes32','bytes32','bytes32']))
funcid = code[:2]+'0'*(10-len(code))+code[2:]
namount=10000
hexstr=hex(namount)[2:]
hamount = '0'*(64-len(hexstr))+hexstr
hexstr=hex(v)[2:]
hv = '0'*(2-len(hexstr))+hexstr
print("allocate('uint256','bytes32','bytes32','bytes32'): ")
print("{0}{1}{2}{3}".format(funcid[2:],hamount,rawhash.encode('hex'),hex(r).strip("L").strip("0x"),hex(s).strip("L").strip("0x")))

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