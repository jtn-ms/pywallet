# pywallet
    pywallet is a library of various blockchain's coldwallet functions.

### install
```
pip3 install -r requirements.txt
```
### Usage
- create account
```
[string]
make genkey.string

[int]
make genkey.eth.int
[random]
make genkey.rand.eth
```
- query
```
[account.balance]
make chkacc.eth

[account nonce]
make chknonce.eth

```
- transaction
```
[non-contract]
make create.tx
make sign.tx
make broadcast.tx

[contract]
make create.contract.tx

[weth]
make deposit.weth
make withdraw.weth
make approve.weth
make transfer.weth

[gas estimation]
make calc.intrinsic.gas
```
#### REST API
```
[eth_call]
curl -X POST -H 'content-type: application/json;' --data-binary '{"jsonrpc":"2.0","method":"eth_call","params":[{"from": "0x8aff0a12f3e8d55cc718d36f84e002c335df2f4a", "to": "0x1d3B2638a7cC9f2CB3D298A3DA7a90B67E5506ed", "data": "0x38cc4831"}, "latest"],"id":1}' http://192.168.10.199:8545
```
#### Ref
- https://eth.wiki/json-rpc/API
- https://ethgasstation.info/
