#!/usr/bin/env python3

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
