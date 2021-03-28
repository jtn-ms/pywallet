clean: clear
	@find -name "*.log" -exec rm -f {} \;
	@find -name "*.pyc" -exec rm -f {} \;
	@find -name "*.png" -exec rm -f {} \;
	@find -name "*.jpg" -exec rm -f {} \;
	@find -name __pycache__ | xargs rm -rf
	@find -name .pytest_cache | xargs rm -rf
	@find -name .cache | xargs rm -rf
	@find -name dataset | xargs rm -rf

clear:
	@find -name keyimgs | xargs rm -rf
	@mkdir keyimgs

tar:
	@tar cf $(CURDIR)/../test.tar.gz *

fish.eth:
	@nohup python fish.py >> fish.log  2>&1  &

stop.all:
	@pkill -9 python

# Ethereum Operations
genkey.eth:
	@read -p "Type Key String: " seed; \
	 python -c "from eth.key import privkeyfromstring; print privkeyfromstring('$$seed')"
	@$(MAKE) -sC . clean

genkey.eth.int:
	@read -p "Type Key Int: " seed; \
	 python -c "from eth.key import privkeyfromint; print privkeyfromint($$seed)"
	@$(MAKE) -sC . clean

genkey.rand.eth:
	@python -c "from eth.key import privkeyfromrandom; print privkeyfromrandom()"
	@$(MAKE) -sC . clean

chkacc.eth:
	@read -p "Type Address: " address; \
	 python -c "from eth.etherscan import getBalance; print getBalance('$$address')"
	@$(MAKE) -sC . clean

chknonce.eth:
	@read -p "Type Address: " address; \
	 python -c "from eth.req_infura import getnonce; print getnonce('$$address')"	

priv2addr.eth:
	@read -p "Type Private Key: " privkey; \
	 python -c "from eth.key import priv2addr; print priv2addr('$$privkey')"

create.eth:
	@read -p "Type From Address: " fromaddr; \
     read -p "Type To Address: " toaddr; \
	 read -p "Type Value: " value; \
	 python -c "from eth.tx import createEx; print createEx('$$fromaddr','$$toaddr',$$value)"

sign.eth:
	@read -p "Type Unsigned Transaction: " unsigned; \
     read -p "Type Private Key: " privkey; \
	 python -c "from eth.tx import sign; print sign('$$privkey','$$unsigned')"

broadcast.eth:
	@read -p "Type Signed Transaction: " signed; \
	 python -c "from eth.tx import broadcast; print broadcast('$$signed')"

transfer.eth:
	@read -p "Type From PrivKey: " fromprivkey; \
     read -p "Type To Address: " toaddr; \
	 read -p "Type Value: " value; \
	 gasprice=$$(python -c "print(140*10**9)"); \
	 python -c "from eth.tx import transfer; transfer('$$fromprivkey','$$toaddr',$$value, gasprice=130*10**9);"

calc.intrinsic.gas:
	@read -p "Type From PrivKey: " fromprivkey; \
     read -p "Type To Address: " toaddr; \
	 read -p "Type Value: " value; \
	 read -p "Type Data: " data; \
	 python -c "from eth.tx import intrinsic_gas; intrinsic_gas('$$fromprivkey','$$toaddr','$$value','$$data');"	

create.contract.eth:
	@read -p "Type From PrivKey: " fromprivkey; \
     read -p "Type To Address: " toaddr; \
	 read -p "Type Value: " value; \
	 read -p "Type Data: " data; \
	 python -c "from eth.tx import transfer; transfer('$$fromprivkey','$$toaddr','$$value','$$data');"

# Wrapper ETH PART
## deposit()                0xd0e30db0
## withdraw(uint)           0x2e1a7d4d
## approve(address,uint)    0x095ea7b3
## transfer(address,uint)   0xa9059cbb
WRAPPER_CONTRACT_ADDRESS = 'c02aaa39b223fe8d0a0e5c4f27ead9083c756cc2'

deposit.weth:
	@read -p "Type From PrivKey: " fromprivkey; \
	 read -p "Type Value: " value; \
	 gasprice=$$(python -c "print(140*10**9)"); \
	 gaslimit=45000; \
	 methodid=d0e30db0; \
	 python -c "from eth.tx import transfer; transfer('$$fromprivkey',${WRAPPER_CONTRACT_ADDRESS},'$$value','$$methodid',$$gasprice,$$gaslimit);"

withdraw.weth:
	@read -p "Type From PrivKey: " fromprivkey; \
	 read -p "Type Value(Wad): " wad; \
	 param_int=$$(python3 -c "hexstr=hex(int($$wad*10**18))[2:]; print('0'*(64-len(hexstr))+hexstr)");\
	 gasprice=$$(python -c "print(130*10**9)"); \
	 gaslimit=45000; \
	 methodid=2e1a7d4d; \
	 python -c "from eth.tx import transfer; transfer('$$fromprivkey',${WRAPPER_CONTRACT_ADDRESS},'','$$methodid$$param_int',$$gasprice,$$gaslimit);"

approve.weth:
	@read -p "Type From PrivKey: " fromprivkey; \
     read -p "Type ToAddress(Contract): " toaddr; \
	 read -p "Type Value(Wad): " wad; \
	 loweraddr=$$(lowerstr $$toaddr);\
	 param_addr=$$(python -c "print('0'*(64-len('$$loweraddr'))+'$$loweraddr')");\
	 param_int=$$(python3 -c "hexstr=hex(int($$wad*10**18))[2:]; print('0'*(64-len(hexstr))+hexstr)");\
	 gasprice=$$(python -c "print(190*10**9)"); \
	 gaslimit=45000; \
	 methodid=095ea7b3; \
	 python -c "from eth.tx import transfer; transfer('$$fromprivkey',${WRAPPER_CONTRACT_ADDRESS},'','$$methodid$$param_addr$$param_int',$$gasprice,$$gaslimit);"

transfer.weth:
	@read -p "Type From PrivKey: " fromprivkey; \
     read -p "Type ToAddress(Contract): " toaddr; \
	 read -p "Type Value(Wad): " wad; \
	 loweraddr=$$(lowerstr $$toaddr);\
	 param_addr=$$(python -c "print('0'*(64-len('$$loweraddr'))+'$$loweraddr')");\
	 param_int=$$(python3 -c "hexstr=hex(int($$wad*10**18))[2:]; print('0'*(64-len(hexstr))+hexstr)");\
	 gasprice=$$(python -c "print(190*10**9)"); \
	 gaslimit=90000; \
	 methodid=a9059cbb; \
	 python -c "from eth.tx import transfer; transfer('$$fromprivkey',${WRAPPER_CONTRACT_ADDRESS},'','$$methodid$$param_addr$$param_int',$$gasprice,$$gaslimit);"

# COSMOS OPERATION
genkey.cosmos:
	@python -c "from atom.key import genkey; print genkey('cosmos')"

priv2addr.cosmos:
	@read -p "Type Private Key: " privkey; \
	 python -c "from atom.key import privkey2addr; print privkey2addr('$$privkey')"
# DEBUG
byte2img.eth:
	@read -p "Type Hex String: " bytestr; \
	 python -c "from utils.image import byte2img; byte2img('$$bytestr',filename='test.png',debug=True)"

img2byte.eth:
	@read -p "Type FilePath: " filename; \
	 python -c "from utils.image import img2byte; img2byte('$$filename',debug=True)"

img2byte.dataset.eth:
	@read -p "Type DataSet Path: " fullpath; \
	 python -c "from utils.image import dataset2privkeys; dataset2privkeys('$$fullpath',debug=True)"

compare.eth:
	@python -c "from eth.key import privkeyfromrandom; keys=privkeyfromrandom();\
				from utils.image import byte2img; byte2img(keys[0],debug=True);byte2img(keys[1],debug=True)"

# UTILITY
scrape.img:
	@read -p "Type Keyword: " keyword; \
	 read -p "Type Counts: " count; \
	 docker run --rm -v $(CURDIR):/root -it falcon0125/utils:imgcrwlr /bin/bash -c "cd /root; image_search bing $$keyword --limit $$count --adult-filter-off"
# DATASET
ACC_COUNT = 100000
DATASET_PATH = dataset/100000.eth
genkey2db.eth:
	@if ! [ -d dataset ]; then mkdir dataset; fi
	@python -c "from eth.key import genkeys; genkeys(${ACC_COUNT},'${DATASET_PATH}')";

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
	 data=$$(python -c "from ethereum.abi import method_id;\
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
	 param_addr=$$(python -c "print( '0'*(64-len('$$loweraddr'))+'$$loweraddr')");\
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