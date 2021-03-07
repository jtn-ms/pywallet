#!/usr/bin/env python

import rlp
import ethereum
import ethereum.transactions


class MyTransaction(ethereum.transactions.Transaction):

    _publickey = None

    @property
    def publickey(self):
        secpk1n = ethereum.transactions.secpk1n
        if not self._publickey:
            if self.v in (27, 28):
                vee = self.v
                rlpdata = rlp.encode(
                    self, ethereum.transactions.UnsignedTransaction)
            elif self.v >= 37:
                vee = self.v - self.network_id * 2 - 8
                assert vee in (27, 28)
                rlpdata = rlp.encode(
                    rlp.infer_sedes(self).serialize(self)[:-3] \
                    + [self.network_id, '', ''])
            else:
                return None  # Invalid V value
            if self.r >= secpk1n or self.s >= secpk1n or self.r == 0 \
                    or self.s == 0:
                return None  # Invalid signature values!
            sighash = ethereum.utils.sha3(rlpdata)
            pub = ethereum.utils.ecrecover_to_pub(sighash, vee, self.r, self.s)
            if pub == b'\x00' * 64:
                return None  # Invalid signature (zero privkey cannot sign)
            self._publickey = pub
        return self._publickey

    @publickey.setter
    def publickey(self, value):
        self._publickey = value


def main():
    nonce = 21
    gasprice = 18000000000
    startgas = 100000
    to = '0xa593094cebb06bf34df7311845c2a34996b52324'
    value = 1000000000000
    data = ''
    sender = "0xc6f4f527587ea4a03aa85e0322783592367c1b9a"
    r = "0xab90122dc4e4bbdbb14ef22ad3ae21aecc19a1c90a9c8989c68b26cc782ff303"
    s ="0x36e5f275147049d3afd5d33b735cc9313d2c1aad3ab401aefdce678128e2f1d0"
    v = "0x1c"
    r = int(r, 16)
    s = int(s, 16)
    v = int(v, 16)
    tx = MyTransaction(nonce, gasprice, startgas, to, value, data, v, r, s)
    print tx.publickey,sender[2:]
    assert sender[2:] == ethereum.utils.sha3(tx.publickey)[-20:].hex()

if __name__ == '__main__':
    main()