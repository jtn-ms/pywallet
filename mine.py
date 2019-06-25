from eth.mine import hunt
from multiprocessing import Process

def mine():
    while True:
        Process(target=hunt).start()
        
if __name__ == "__main__":
    mine()