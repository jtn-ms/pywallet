from sha3 import keccak_256
from ethereum.abi import encode_single,encode_abi
from rlp.utils import decode_hex,encode_hex

def createAddr(addr,nonce):
    encoded = encode_abi(('bytes32','uint64'),(addr.decode("hex"),long(nonce)))
    print(encoded.encode('hex'))
    contractAddr = keccak_256(encoded).digest()[12:]
    print(contractAddr.encode('hex'))
    return contractAddr

from ethereum.utils import privtoaddr,privtopub

def genAddr(prefix,suffix):
    decoded=prefix + ((64-len(prefix))/len(suffix))*suffix
    encoded=decoded.decode("hex")
    privkey = keccak_256(encoded).digest()
    addr = privtoaddr(encoded)
    # contractAddr = keccak_256(encoded).digest()[-20:]
    print(encode_hex(addr))

if __name__ == "__main__":
    # createAddr("b20a608c624ca5003905aa834de7156c68b2e1d0",0)
    # genAddr("b20a608c624ca5003905aa834de7156c68b2e1d0","0")
    genAddr("00000000000000000000000000000000000000","ff")