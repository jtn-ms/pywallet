from ethereum.transactions import Transaction,UnsignedTransaction
import rlp

class TransactionEx(Transaction):
    @property
    def unsigned(self):
        return rlp.encode(self, UnsignedTransactionEx)

UnsignedTransactionEx = TransactionEx.exclude(['v', 'r', 's'])