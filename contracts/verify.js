var Example = artifacts.require('./verify.sol')

var Web3 = require('web3')
var web3 = new Web3(new Web3.providers.HttpProvider('http://localhost:8545'))

contract('Example', (accounts) => {
  var address = accounts[0]

  it('ecrecover result matches address', async function() {
    var instance = await Example.deployed()
    var msg = '0x8CbaC5e4d803bE2A3A5cd3DbE7174504c6DD0c1C'

    var h = web3.sha3(msg)
    var sig = web3.eth.sign(address, h).slice(2)
    var r = `0x${sig.slice(0, 64)}`
    var s = `0x${sig.slice(64, 128)}`
    var v = web3.toDecimal(sig.slice(128, 130)) + 27

    var result = await instance.testRecovery.call(h, v, r, s)
    assert.equal(result, address)
  })
})