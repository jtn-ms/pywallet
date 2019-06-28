# written by junying, 2019-06-27
# strategy 1: random hunt
# strategy 2: dictionary hunt(meaningful words or sentence)
# strategy 3: dictionary hunt(meaningful image or mark) 
# strategy 4: neural network based hunt(gan-crack AES)

if __name__ == "__main__":
    from key import privkeyfromrandom,privkeyfromstring
    from req import getbalance
else:
    from eth.key import privkeyfromrandom,privkeyfromstring
    from eth.req import getbalance
import os

def shot(keystr=None):
    addr,privkey = privkeyfromstring(keystr) if keystr else privkeyfromrandom()
    balance = getbalance(addr)
    if balance >= 0.01: os.system('echo ETH\t{0}\t{1}\t{2} >> fish.list'.format(addr,privkey,balance))
    else: print('ETH\t{0}\t{1}\t{2}'.format(addr,privkey,balance))

if __name__ == "__main__":
    shot()