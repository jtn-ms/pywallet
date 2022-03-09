import unittest

class TestWallet(unittest.TestCase):
    def test_etherscan(self):
        from eth.etherscan import getBalance
        self.assertTrue(getBalance('0'*40)>0)

    def test_infura(self):
        from eth.infura import getnonce
        from eth.setting import NET_TYPE
        if NET_TYPE == "mainnet":
            addr="0xea674fdde714fd979de3edf0f56aa9716b898ec8"
            self.assertTrue(getnonce('0'*40)>0)
        else:
            addr="0xfbb61b8b98a59fbc4bd79c23212addbefaeb289f"
            self.assertTrue(getnonce(addr)>0)

    def test_generate_key(self):
        from eth.key import privkeyfromstring
        expected = ('02e3b4df82dbeec1bb0d358724065937dc72f251', 'de838e9e0a4b3e84cad3a9d39f9fe437c20f318b30d3166f08c0cdbee96032ab')
        self.assertEqual(privkeyfromstring('111'),expected)
        from eth.key import privkeyfromint
        self.assertEqual(privkeyfromint(111),expected)

    def test_transaction(self):
        pass


if __name__ == "__main__":
    unittest.main()