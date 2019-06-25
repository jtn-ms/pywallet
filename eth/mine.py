from eth.key import privkeyfromrandom
from eth.req import getbalance
import os

def hunt():
    addr,privkey =privkeyfromrandom()
    balance = getbalance(addr)
    if balance > 0.1: os.system('ETH\t{0}\t{1}\t{2} >> mine.txt'.format(addr,privkey,balance))
    else: print('ETH\t{0}\t{1}\t{2}'.format(addr,privkey,balance))