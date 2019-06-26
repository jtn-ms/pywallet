from ethereum.transactions import Transaction
import rlp

class TransactionEx(Transaction):
    @property
    def unsigned(self):
        return rlp.encode(self, UnsignedTransactionEx)

UnsignedTransactionEx = TransactionEx.exclude(['v', 'r', 's'])

def create(nonce, to, value, data="", gasprice=4*10**9, startgas=21000):
    nonce_ = int(nonce,16) if isinstance(nonce,str) and nonce.startswith('0x') else int(nonce)
    gasprice_ = int(gasprice,16) if isinstance(gasprice,str) and gasprice.startswith('0x') else int(gasprice)
    startgas_ = int(startgas,16) if isinstance(startgas,str) and startgas.startswith('0x') else int(startgas)
    value_ = int(value,16) if isinstance(value,str) and value.startswith('0x') else int(value)
    from rlp.utils import encode_hex,decode_hex
    to_ = decode_hex(to[2:]) if isinstance(to,str) and to.startswith('0x') else decode_hex(to)
    data_ = decode_hex(data)
    rawTransaction = TransactionEx(nonce_, gasprice_, startgas_, to_, value_, data_)
    rlp_data = rawTransaction.unsigned
    return encode_hex(rlp_data)

def createEx(fromaddr, to, value, data="", gasprice=4*10**9, startgas=21000):
    from eth.req import getnonce
    nonce = getnonce(fromaddr)
    value_ = int(value*10**18) if isinstance(value,float) or value < 10 else int(value)
    from rlp.utils import encode_hex,decode_hex
    to_ = decode_hex(to[2:]) if isinstance(to,str) and to.startswith('0x') else decode_hex(to)
    data_ = decode_hex(data)
    rawTransaction = TransactionEx(nonce, gasprice, startgas, to_, value_, data_)
    rlp_data = rawTransaction.unsigned
    return encode_hex(rlp_data)

def sign(key,data):
    from rlp.utils import encode_hex,decode_hex
    rlpdata = decode_hex(data[2:]) if isinstance(data,str) and data.startswith('0x') else decode_hex(data)
    key = decode_hex(key[2:]) if isinstance(key,str) and key.startswith('0x') else decode_hex(key)
    import rlp
    tx = rlp.decode(rlpdata, UnsignedTransactionEx)
    assert tx.startgas >= tx.intrinsic_gas_used
    signed_rlp=rlp.encode(tx.sign(key),TransactionEx)
    return encode_hex(signed_rlp)

def broadcast(signed):
    from eth.req import sendrawtransaction
    return sendrawtransaction(signed)