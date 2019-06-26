clean:
	@find -name mine.log -exec rm -f {} \;
	@find -name "*.pyc" -exec rm -f {} \;
	@find -name __pycache__ | xargs rm -rf
	@find -name .pytest_cache | xargs rm -rf
	@find -name .cache | xargs rm -rf

mine:
	@nohup python mine.py >> mine.log  2>&1  &

tar:
	@tar cf $(CURDIR)/../test.tar.gz *

stop:
	@pkill -9 python

priv2addr.eth:
	@read -p "Type Private Key: " privkey; \
	 python -c "from eth.key import priv2addr; print priv2addr('$$privkey')"

chkacc.eth:
	@read -p "Type Address: " addr; \
	 python -c "from eth.req import getbalance; print getbalance('$$addr')"	