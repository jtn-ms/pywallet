from eth.mine import hunt

def mine():
    while True:
        hunt()
        
if __name__ == "__main__":
    mine()