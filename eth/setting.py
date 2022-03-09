
#!/usr/bin/env python3
import toml
import yaml
import os

def loadyaml(filepath):
    with open(os.path.abspath(filepath)) as f:
        try:
            config = yaml.safe_load(f)
            return config
        except yaml.YAMLError as e: return {}
    
config=loadyaml('setting.yaml')
if not config: os.exit()
NET_TYPE = config["network"]

try:
    import os
    parsed=toml.load(os.path.abspath("apis/apis.toml"))
    ETHERSCAN_API_URL = config[NET_TYPE]["etherscan"]
    ETHERSCAN_KEY = parsed["etherscan"][NET_TYPE]
    INFURA_KEY = parsed["infura"][NET_TYPE]
    INFURA_URL = config[NET_TYPE]["infura"]
    INFURA_SIGNED_URL = INFURA_URL+INFURA_KEY
except toml.TomlDecodeError: 
    print("TomlDecodeError")
    import sys
    # assert(False,"TomlDecodeError")
    # sys.exit()

if __name__ == "__main__":
    print(ETHERSCAN_KEY)
    print(ETHERSCAN_API_URL)