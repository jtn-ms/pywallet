from ethereum.utils import privtoaddr,privtopub
from rlp.utils import decode_hex,encode_hex
from ethereum.tools.keys import decode_keystore_json
from ethereum.tools.keys import make_keystore_json
from eth.key import makekeyfile

def test_key():
    passwd = '123'
    encrypted = makekeyfile(passwd)
    assert(encode_hex(encrypted[0]) == encode_hex(decode_keystore_json(encrypted[1],passwd)))