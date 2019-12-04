if __name__ == "__main__":
    from utils import int2hex,normalize_addr,normalize_privaddr
else:
    from research.utils import int2hex,normalize_addr,normalize_privaddr
from ethereum.utils import privtoaddr
from rlp.utils import decode_hex,encode_hex

def test():
    privkeys = [i*64 for i in "123456789abcdef"]
    for privkey in privkeys:
        addr = privtoaddr(decode_hex(privkey)).encode('hex')
        print(privkey)
        print(addr)
        print(normalize_privaddr(privkey))
        print(normalize_addr(addr))

if __name__ == "__main__":
    test()