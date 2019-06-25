from ethereum.transactions import Transaction,UnsignedTransaction
import rlp

class TransactionEx(Transaction):
    @property
    def unsigned(self):
        return rlp.encode(self, UnsignedTransactionEx)

UnsignedTransactionEx = TransactionEx.exclude(['v', 'r', 's'])

def create(nonce, gasprice, startgas, to, value, data):
    nonce_ = int(nonce,16) if isinstance(nonce,str) and '0x' in nonce else int(nonce)
    gasprice_ = int(gasprice,16) if isinstance(gasprice,str) and '0x' in gasprice else int(gasprice)
    startgas_ = int(startgas,16) if isinstance(startgas,str) and '0x' in startgas else int(startgas)
    value_ = int(value,16) if isinstance(value,str) and '0x' in value else int(value)
    from rlp.utils import encode_hex,decode_hex
    to_ = decode_hex(to[2:]) if isinstance(to,str) and '0x' in to else decode_hex(to)
    data_ = decode_hex(data)
    rawTransaction = TransactionEx(nonce_, gasprice_, startgas_, to_, value_, data_)
    rlp_data = rawTransaction.unsigned
    return encode_hex(rlp_data)

def sign(key,data):
    from rlp.utils import encode_hex,decode_hex
    rlpdata = decode_hex(data[2:]) if isinstance(data,str) and '0x' in data else decode_hex(data)
    key = decode_hex(key[2:]) if isinstance(key,str) and '0x' in key else decode_hex(key)
    import rlp
    tx = rlp.decode(rlpdata, UnsignedTransactionEx)
    assert tx.startgas >= tx.intrinsic_gas_used
    signed_rlp=rlp.encode(tx.sign(key),TransactionEx)
    return encode_hex(signed_rlp)

# from wallets such as metamask, imtoken
# metamask: https://metamask.github.io/metamask-docs/API_Reference/JSON_RPC_API
#           https://api.infura.io/v1/jsonrpc/mainnet/eth_sendRawTransaction?params=0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675
#           https://github.com/MetaMask/metamask-extension/blob/18179fd34551680bd65df7c0c3caaa5945d1e94d/ui/app/pages/settings/networks-tab/networks-tab.constants.js
#           curl http://api.infura.io/v1/jsonrpc/main/eth_sendRawTransaction?params=0xd46e8dd67c5d32be8d46e8dd67c5d32be8058bb8eb970870f072445675058bb8eb970870f072445675
# & etherscan apis
# eth_sendRawTransaction: https://api.etherscan.io/api?module=proxy&action=eth_sendRawTransaction&hex=0xf904808000831cfde080&apikey=YourApiKeyToken
# 
def broadcast():
    pass