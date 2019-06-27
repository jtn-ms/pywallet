from eth.mine import shot
from multiprocessing import Process

def randtry():
    while True:
        Process(target=shot).start()
        
def primetry():
    for i in range(2,1024):
        if i % 2 == 0: continue
        Process(target=shot,args=(str(2**i-1),)).start()
        
if __name__ == "__main__":
    primetry()