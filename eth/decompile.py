from sha3 import keccak_256
from ethereum.abi import encode_single,encode_abi
from rlp.utils import decode_hex,encode_hex

def createAddr(addr,nonce):
    encoded = encode_abi(('bytes32','uint64'),(addr.decode("hex"),long(nonce)))
    print(encoded.encode('hex'))
    contractAddr = keccak_256(encoded).digest()[12:]
    print(contractAddr.encode('hex'))
    return contractAddr

# sha3(0xff ++ msg.sender ++ salt ++ sha3(init_code))[12:]
def createAddr2(addr,salt,init_code):
    pass

from ethereum.utils import privtoaddr,privtopub
try:
    from eth.etherscan import getBalance
except:
    from etherscan import getBalance

def genAddr(prefix,suffix):
    suffix = hex(suffix) if isinstance(suffix,int) else suffix
    suffix = suffix.strip("0x")
    decoded=prefix + (64-len(prefix) -len(suffix)) * '0' + suffix
    print("decoded: {0}".format(decoded))
    encoded=decoded.decode("hex")
    # privkey = keccak_256(encoded).digest()
    addr = privtoaddr(encoded)
    # contractAddr = keccak_256(encoded).digest()[-20:]
    hexaddr=encode_hex(addr)
    balance=getBalance(hexaddr)/1.0/10**18
    if balance > 0.1: print("{0}-{1}".format(hexaddr, balance))

# 1000000000000000000000000000000000000000000000000000000000000000
if __name__ == "__main__":
    # createAddr("4f26ffbe5f04ed43630fdc30a87638d53d0b0876",446)
    for i in range(64):
        genAddr("0"*i+"1", 0)
    # genAddr("00000000000000000000000000000000000000","ff")