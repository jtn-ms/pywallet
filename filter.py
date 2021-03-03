from os import walk
from eth.req import getbalance

_, _, filenames = next(walk("tmp"))

skey="Z--"

# filtering
accounts = []
for filename in filenames:
    try:
        sidx = filename.index(skey) + len(skey)
    except:
        sidx = -2
    if sidx < 0: continue    
    account = filename[sidx:]
    accounts.append("{0}--{1}\n".format(account,getbalance(account)))

file2 = open('acc.lst', 'w')
file2.writelines(accounts)
file2.close()