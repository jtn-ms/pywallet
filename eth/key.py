# -*- coding: utf-8 -*-
"""
$ python utils.py UTC--2019-03-14T08-21-57.582333053Z--a69cbac58e16f007cb553a59651725fed671c335 123
c9cd37e7d47825219002a06bdb2debcb73d89c15b6a50c1f332d4985a62b2610
"""

from ethereum.utils import sha3
from ethereum.utils import privtoaddr,privtopub
from rlp.utils import decode_hex,encode_hex

def privkeyfromstring(string='dog'):
    privkey = sha3(string)
    # pubkey = privtopub(privkey)
    addr = privtoaddr(privkey)
    return encode_hex(addr),encode_hex(privkey)

def privkeyfromint(value):
    privkey = sha3(value)
    addr = privtoaddr(privkey)
    return encode_hex(addr),encode_hex(privkey)

def privkeyfromrandom():
    import os
    privkey = os.urandom(32)
    addr = privtoaddr(privkey)
    return addr.encode('hex'),privkey.encode('hex')

# 2**(16**2)
# my fortune reaches to at most double or triple.
# 256 wins in binary option is unimaginable.
# FREQUENCY IS GOD
def privkeyfrombinary():
    pass

def genkey(keystring=''):
    return privkeyfromstring(keystring) if keystring else privkeyfromrandom()

import multiprocessing
from functools import partial
def genkeys(count=10,filepath=None):
    accs = []
    pool = multiprocessing.Pool(multiprocessing.cpu_count())
    outputs = pool.map(genkey,['']*count)
    for output in outputs:
        addr,privkey=output
        accs.append('{0}\t{1}\n'.format(addr,privkey))
    if filepath:
        with open(filepath,'w') as file:
            file.writelines(accs)
            
def priv2addr(privkey):
    return encode_hex(privtoaddr(decode_hex(privkey)))

from ethereum.tools.keys import decode_keystore_json
from ethereum.tools.keys import make_keystore_json

def privkeyfromfile(filename,passwd):
    with open(filename) as f:
        import json
        data = json.load(f)
        return encode_hex(decode_keystore_json(data,passwd))

def decryptkeyfile():
    import sys
    if len(sys.argv) > 2:
        privkey = privkeyfromfile(sys.argv[1],sys.argv[2])
        print(privkey)
        print(privtoaddr(decode_hex(privkey)))
        
def makekeyfile(passwd):
    import os
    priv = os.urandom(32)
    encrypted=make_keystore_json(priv=priv,pw=passwd,kdf="pbkdf2", cipher="aes-128-ctr")
    return priv,encrypted

if __name__ == "__main__":
    decryptkeyfile()