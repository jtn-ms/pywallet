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
	 python -c "from eth.req import getbalance; print getbalance('$$address')"
	@$(MAKE) -sC . clean

chknonce.eth:
	@read -p "Type Address: " address; \
	 python -c "from eth.req import getnonce; print getnonce('$$address')"	

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
	 python -c "from eth.tx import transfer; transfer('$$fromprivkey','$$toaddr',$$value);"

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