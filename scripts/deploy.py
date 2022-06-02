from brownie import Token, accounts
from web3 import Web3


def deploy():

    t = Token.deploy("DOGU TEST", "DOU", 18, 1e21, {"from": accounts[0]})
    print(f"eth balance acc 0 is {t.contractEthBalance(accounts[0])}")
    add = t.address
    print(f"t balance{t.balance()}")
    print(f"account 0 balance{ t.balanceOf(accounts[0])}")
    t.transfer(accounts[3], 10 * 10**18, {"from": accounts[0]})
    print(f"account 0 balance{ t.balanceOf(accounts[0])}")
    # t.balanceOf(accounts[3])
    print(f"account 5 balance{ t.balanceOf(accounts[5])}")
    print(f"account 3 balance{ t.balanceOf(accounts[3])}")
    print(f"account 0 balance{ t.balanceOf(accounts[0])}")
    # approve account3 e account0 dan 5 token cekme yetkisi veriyor
    t.approve(accounts[3], 5 * 10**18, {"from": accounts[0]})
    print(f" allowence account3 is: {t.allowance(accounts[0],accounts[3])}")
    print(f"account 5 balance{ t.balanceOf(accounts[5])}")
    print(f"account 3 balance{ t.balanceOf(accounts[3])}")
    print(f"account 0 balance{ t.balanceOf(accounts[0])}")
    # accout3 account0 dan 3 token cekip 5 aktariyor
    print(f"t balance{t.balanceOf(add)}")
    print(f"eth balance {t.contractEthBalance(add)}")
    t.transferSelf({"value": Web3.toWei(1, "ether"), "from": accounts[0]})
    t.transferFrom(accounts[0], accounts[5], 3 * 10**18, {"from": accounts[3]})
    t.transferFrom(accounts[0], add, 2 * 10**18, {"from": accounts[3]})
    print(f"t balance{t.balanceOf(add)}")
    print(f"eth balance {t.contractEthBalance(add)}")
    print(f"account 5 balance{ t.balanceOf(accounts[5])}")
    print(f"account 3 balance{ t.balanceOf(accounts[3])}")
    print(f"account 0 balance{ t.balanceOf(accounts[0])}")

    # function approve(address _spender, uint256 _value) public returns (bool) {
    #
    # function transferFrom( address _from,address _to,uint256 _value)
    #
    #  owner->spender
    # allowed[msg.sender][_spender] = _value;
    #


def main():
    deploy()
