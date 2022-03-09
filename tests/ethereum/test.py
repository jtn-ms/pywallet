import unittest

class TestEthereum(unittest.TestCase):
    def test_makekeyfile(self):
        from ethereum.utils import privtoaddr,privtopub
        from rlp.utils import decode_hex,encode_hex
        from ethereum.tools.keys import decode_keystore_json
        from ethereum.tools.keys import make_keystore_json
        from eth.key import makekeyfile
        passwd = '123'
        encrypted = makekeyfile(passwd)
        assert(encode_hex(encrypted[0]) == encode_hex(decode_keystore_json(encrypted[1],passwd)))
    
    def test_ecrecover(self):
        from ethereum.utils import sha3,normalize_key
        from ethereum.utils import privtoaddr,privtopub
        from ethereum.utils import ecsign,ecrecover_to_pub
        from rlp.utils import decode_hex,encode_hex
        privkey = sha3("test")
        signedaddr = privtoaddr(privkey)
        data = "this is the message to be encrypted".encode('utf-8')
        # encryption
        from sha3 import keccak_256
        rawhash = keccak_256(data).digest()
        v, r, s = ecsign(rawhash, normalize_key(privkey))
        p_r = hex(r).strip("L").strip("0x")
        p_s = hex(s).strip("L").strip("0x")
        p_h = encode_hex(rawhash)
        x_r = '0'*(64-len(p_r))+p_r
        x_s = '0'*(64-len(p_s))+p_s
        x_h = '0'*(64-len(p_h))+p_h
        # decryption
        pubkey = ecrecover_to_pub(rawhash,v,r,s)
        signer = keccak_256(pubkey).digest()[-20:]
        # compare
        self.assertEqual(signer,signedaddr)

    # dice2.win.sol
    # Function: placeBet(uint256 betMask, uint256 modulo, uint256 commitLastBlock, uint256 commit, bytes32 r, bytes32 s)
    # MethodID: 0x5e83b463
    # O[0]:  0000000000000000000000000000000000000000000000000000000000000038
    # O[1]:  0000000000000000000000000000000000000000000000000000000000000006
    # X[2]:  0000000000000000000000000000000000000000000000000000000000b72503
    # X[3]:  8a68b68093f41d77e17c341a9a8a79585f5ce7ced41d1dcbe5f5f770476d7fdd
    # X[4]:  e6118f75e7c18033d019e3f5490f9be37d2becd82eb643eaf7fe10c7fd27fa4f
    # X[5]:  057089906b666936a8be0d52c5558e7c83cbe5f27fbca4a21531dc38ea7ca24a
    ######################
    # // Check that commit is valid - it has not expired and its signature is valid.
    # require (block.number <= commitLastBlock, "Commit has expired.");
    # bytes32 signatureHash = keccak256(abi.encodePacked(uint40(commitLastBlock), commit));
    # require (secretSigner == ecrecover(signatureHash, 27, r, s), "ECDSA signature is not valid.");
    def test_ecrecover_case(self):
        commitLastBlock = "0000000000000000000000000000000000000000000000000000000000b7270d"
        commit = "e021e8dd8ae038b0414a80100de5048f2996b9fd247d0cdb1fe480c567edfb6f"
        _r = "d4af6c87392704cf891c5af466c4fb31706454e92122deee475dd0b6b0a09687"
        _s = "00cef18ff00f8562ffe7ab1bc0afce0f2b757c6a3c360fe8c03b9dd6be62e93e"

        nblkid = int(commitLastBlock.strip("0"),16)
        print("nblkid: {0}".format(nblkid))
        import hashlib
        import binascii
        from ethereum.abi import encode_single,encode_abi
        from sha3 import keccak_256
        from rlp.utils import decode_hex,encode_hex
        # from eth_hash.auto import keccak
        print("#################### ecrecover testing(based on dice2.win's tx data)#####################")
        encoded = encode_abi(('uint40','uint256'),(int(commitLastBlock,16),int(commit,16)))
        _rawhash=keccak_256(encoded).digest()
        # print("_rawhash: {0}-{1}-{2}".format(_rawhash,type(_rawhash),len(_rawhash)))
        _rawhashstr=hashlib.sha256(encoded).hexdigest()
        # decryption
        from ethereum.utils import ecsign,ecrecover_to_pub
        v=27
        pubkey = ecrecover_to_pub(_rawhash,v,int(_r,16),int(_s,16))
        signer = keccak_256(pubkey).digest()[-20:]
        self.assertEqual(encode_hex(signer),"5483fca3be2a62c2cbb581e2816837a7081d8bc1")

    def test_v27(self):
        import rlp
        import ethereum
        import ethereum.transactions
        nonce = 21
        gasprice = 125*10**9
        startgas = 100000
        to = ''
        value = int(0.02 * 10**18)
        data = ''
        sender = "0xc6f4f527587ea4a03aa85e0322783592367c1b9a"
        r = "0xab90122dc4e4bbdbb14ef22ad3ae21aecc19a1c90a9c8989c68b26cc782ff303"
        s ="0x36e5f275147049d3afd5d33b735cc9313d2c1aad3ab401aefdce678128e2f1d0"
        v = "0x1c"
        r = int(r, 16)
        s = int(s, 16)
        v = int(v, 16)
        from eth.tx2 import MyTransaction
        tx = MyTransaction(nonce, gasprice, startgas, to, value, data, v, r, s)
        from rlp.utils import decode_hex,encode_hex
        retrieved=encode_hex(ethereum.utils.sha3(tx.publickey)[-20:])
        print(type(sender),type(retrieved))
        print(sender,retrieved)
        print(sender[2:])
        self.assertEqual(sender[2:],retrieved)
    # https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md
    # CHAIN_ID	Chain(s)
    # 1	        Ethereum mainnet
    # 2	        Morden (disused), Expanse mainnet
    # 3	        Ropsten
    # 4	        Rinkeby
    # 5	        Goerli
    # 42	    Kovan
    # 1337	    Geth private chains (default)
    def test_v37(self):
        import rlp
        import ethereum
        import ethereum.transactions
        nonce = 9
        gasprice = 20*10**9
        startgas = 21000
        to = '0x3535353535353535353535353535353535353535'
        value = int(1 * 10**18)
        data = ''
        sender = "0x9d8a62f656a8d1615c1294fd71e9cfb3e4855a4f"
        r = "0xab90122dc4e4bbdbb14ef22ad3ae21aecc19a1c90a9c8989c68b26cc782ff303"
        s ="0x36e5f275147049d3afd5d33b735cc9313d2c1aad3ab401aefdce678128e2f1d0"
        v = '0x25'#"0x1c", 27->37 according to https://github.com/ethereum/EIPs/blob/master/EIPS/eip-155.md
        r = 18515461264373351373200002665853028612451056578545711640558177340181847433846#int(r, 16)
        s = 46948507304638947509940763649030358759909902576025900602547168820602576006531#int(s, 16)
        v = 37#int(v, 16)
        from eth.tx2 import MyTransaction
        tx = MyTransaction(nonce, gasprice, startgas, to, value, data, v, r, s)
        from rlp.utils import decode_hex,encode_hex
        retrieved=encode_hex(ethereum.utils.sha3(tx.publickey)[-20:])
        print(type(sender),type(retrieved))
        print(sender,retrieved)
        print(sender[2:])
        self.assertEqual(sender[2:],retrieved)

if __name__ == "__main__":
    unittest.main()