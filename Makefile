clean:
	@find -name "*.log" -exec rm -f {} \;
	@find -name "*.pyc" -exec rm -f {} \;
	@find -name "*.png" -exec rm -f {} \;
	@find -name __pycache__ | xargs rm -rf
	@find -name .pytest_cache | xargs rm -rf
	@find -name .cache | xargs rm -rf
	@find -name dataset | xargs rm -rf

# Ethereum Operations
genkey.string:
	@read -p "Type Key String: " seed; \
	 python3 -c "from eth.key import privkeyfromstring; print(privkeyfromstring('$$seed'))"
	@$(MAKE) -sC . clean

genkey.eth.int:
	@read -p "Type Key Int: " seed; \
	 python3 -c "from eth.key import privkeyfromint; print(privkeyfromint($$seed))"
	@$(MAKE) -sC . clean

genkey.rand.eth:
	@python3 -c "from eth.key import privkeyfromrandom; print(privkeyfromrandom())"
	@$(MAKE) -sC . clean

chkacc.eth:
	@read -p "Type Address: " address; \
	 python3 -c "from eth.etherscan import getBalance; print(getBalance('$$address'))"
	@$(MAKE) -sC . clean

chknonce.eth:
	@read -p "Type Address: " address; \
	 python3 -c "from eth.infura import getnonce; print(getnonce('$$address'))"	

priv2addr.eth:
	@read -p "Type Private Key: " privkey; \
	 python3 -c "from eth.key import priv2addr; print(priv2addr('$$privkey'))"

create.tx:
	@read -p "Type From Address: " fromaddr; \
     read -p "Type To Address: " toaddr; \
	 read -p "Type Value: " value; \
	 python3 -c "from eth.tx import createEx; print(createEx('$$fromaddr','$$toaddr',$$value))"

sign.tx:
	@read -p "Type Unsigned Transaction: " unsigned; \
     read -p "Type Private Key: " privkey; \
	 python3 -c "from eth.tx import sign; print(sign('$$privkey','$$unsigned'))"

broadcast.tx:
	@read -p "Type Signed Transaction: " signed; \
	 python3 -c "from eth.tx import broadcast; print(broadcast('$$signed'))"

transfer.tx:
	@read -p "Type From PrivKey: " fromprivkey; \
     read -p "Type To Address: " toaddr; \
	 read -p "Type Value: " value; \
	 python3 -c "from eth.tx import transfer; transfer('$$fromprivkey','$$toaddr',$$value, gasprice=125*10**9);"

calc.intrinsic.gas:
	@read -p "Type From PrivKey: " fromprivkey; \
     read -p "Type To Address: " toaddr; \
	 read -p "Type Value: " value; \
	 read -p "Type Data: " data; \
	 python3 -c "from eth.tx import intrinsic_gas; intrinsic_gas('$$fromprivkey','$$toaddr','$$value','$$data');"	

create.contract.tx:
	@read -p "Type From PrivKey: " fromprivkey; \
     read -p "Type To Address: " toaddr; \
	 read -p "Type Value: " value; \
	 read -p "Type Data: " data; \
	 python3 -c "from eth.tx import transfer; transfer('$$fromprivkey','$$toaddr','$$value','$$data');"

# Wrapper ETH PART
## deposit()                0xd0e30db0
## withdraw(uint)           0x2e1a7d4d
## approve(address,uint)    0x095ea7b3
## transfer(address,uint)   0xa9059cbb
WRAPPER_CONTRACT_ADDRESS = 'c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'

deposit.weth:
	@read -p "Type From PrivKey: " fromprivkey; \
	 read -p "Type Value: " value; \
	 gasprice=$$(python3 -c "print(140*10**9)"); \
	 gaslimit=45000; \
	 methodid=d0e30db0; \
	 python3 -c "from eth.tx import transfer; transfer('$$fromprivkey',${WRAPPER_CONTRACT_ADDRESS},'$$value','$$methodid',$$gasprice,$$gaslimit);"

withdraw.weth:
	@read -p "Type From PrivKey: " fromprivkey; \
	 read -p "Type Value(Wad): " wad; \
	 param_int=$$(python3 -c "hexstr=hex(int($$wad*10**18))[2:]; print('0'*(64-len(hexstr))+hexstr)");\
	 gasprice=$$(python3 -c "print(140*10**9)"); \
	 gaslimit=45000; \
	 methodid=2e1a7d4d; \
	 python3 -c "from eth.tx import transfer; transfer('$$fromprivkey',${WRAPPER_CONTRACT_ADDRESS},'','$$methodid$$param_int',$$gasprice,$$gaslimit);"

approve.weth:
	@read -p "Type From PrivKey: " fromprivkey; \
     read -p "Type ToAddress(Contract): " toaddr; \
	 read -p "Type Value(Wad): " wad; \
	 loweraddr=$$(lowerstr $$toaddr);\
	 param_addr=$$(python3 -c "print('0'*(64-len('$$loweraddr'))+'$$loweraddr')");\
	 param_int=$$(python3 -c "hexstr=hex(int($$wad*10**18))[2:]; print('0'*(64-len(hexstr))+hexstr)");\
	 gasprice=$$(python3 -c "print(140*10**9)"); \
	 gaslimit=45000; \
	 methodid=095ea7b3; \
	 python3 -c "from eth.tx import transfer; transfer('$$fromprivkey',${WRAPPER_CONTRACT_ADDRESS},'','$$methodid$$param_addr$$param_int',$$gasprice,$$gaslimit);"

transfer.weth:
	@read -p "Type From PrivKey: " fromprivkey; \
     read -p "Type ToAddress(Contract): " toaddr; \
	 read -p "Type Value(Wad): " wad; \
	 loweraddr=$$(lowerstr $$toaddr);\
	 param_addr=$$(python3 -c "print('0'*(64-len('$$loweraddr'))+'$$loweraddr')");\
	 param_int=$$(python3 -c "hexstr=hex(int($$wad*10**18))[2:]; print('0'*(64-len(hexstr))+hexstr)");\
	 gasprice=$$(python3 -c "print(120*10**9)"); \
	 gaslimit=90000; \
	 methodid=a9059cbb; \
	 python3 -c "from eth.tx import transfer; transfer('$$fromprivkey',${WRAPPER_CONTRACT_ADDRESS},'','$$methodid$$param_addr$$param_int',$$gasprice,$$gaslimit);"

# create method_id
# from ethereum.abi import method_id
# hex(method_id("minter",[]))
# hex(method_id("balances",['address']))
# hex(method_id("mint",['address','uint256']))
# hex(method_id("send",['address','uint256']))
# Usage:
# function name: minter
# parameters: 
# function name: mint
# parameters: 'address','uint256'
get.method.id:
	@read -p "function name: " funcname;\
	 read -p "parameters: " paramstr;\
	 data=$$(python3 -c "from ethereum.abi import method_id;\
	 				 	code=hex(method_id('$$funcname',[$$paramstr]));\
						print(code[:2]+'0'*(10-len(code))+code[2:]);\
						");\
	 echo $$data

# param: address
# In:  htdf1ha7ryup8nc2avgesfunx2pm22waqv2cx6dj0ac
# Out: BF7C3270279E15D623304F2665076A53BA062B06
# 	   bf7c3270279e15d623304f2665076a53ba062b06
#	   000000000000000000000000bf7c3270279e15d623304f2665076a53ba062b06
param.address:
	@read -p "byteaddr: " byteaddr;\
	 loweraddr=$$(lowerstr $$byteaddr);\
	 param_addr=$$(python3 -c "print( '0'*(64-len('$$loweraddr'))+'$$loweraddr')");\
	 echo $$param_addr

# param: int
# In:  100000
# Out: 
# 	   
#	   
param.int:
	@read -p "uint: " uint;\
	 python3 -c "hexstr=hex($$uint)[2:];\
	 			 print('0'*(64-len(hexstr))+hexstr)"

# In:aaa
# Out:0000000000000000000000000000000000000000000000000000000000616161
param.string:
	@read -p "string: " string;\
	 python3 -c "hexstr=b'$$string'.hex();\
	 			 print('0'*(64-len(hexstr))+hexstr)"

# In:616161
# Out:aaa
hex2str:
	@read -p "hexstr: " hexstr;\
	 python3 -c "string=bytes.fromhex('$$hexstr').decode('utf-8') ;\
	 			 print(string)"

test.ethereum:
	@python3 -m unittest discover -s tests/ethereum

test.wallet:
	@python3 -m unittest discover -s tests/wallet

test: test.ethereum test.wallet