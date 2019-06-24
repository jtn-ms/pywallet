"""
$ python utils.py UTC--2019-03-14T08-21-57.582333053Z--a69cbac58e16f007cb553a59651725fed671c335 123
c9cd37e7d47825219002a06bdb2debcb73d89c15b6a50c1f332d4985a62b2610
"""

from ethereum.utils import sha3
from ethereum.utils import privtoaddr,privtopub
from rlp.utils import decode_hex,encode_hex

def privkeyfromstring(string='dog'):
    privkey = sha3(string)
    pubkey = privtopub(privkey)
    addr = privtoaddr(privkey)
    return encode_hex(addr),encode_hex(privkey),pubkey

def privkeyfromfile(filename,passwd):
    with open(filename) as f:
        import json
        data = json.load(f)
        from ethereum.tools.keys import decode_keystore_json
        from rlp.utils import encode_hex
        return encode_hex(decode_keystore_json(data,passwd))

def test_get_privkey():
    import sys
    if len(sys.argv) > 2:
        privkey = privkeyfromfile(sys.argv[1],sys.argv[2])
        print(privkey)
        print(privtoaddr(decode_hex(privkey)))
        
if __name__ == "__main__":
    print(privkeyfromstring())