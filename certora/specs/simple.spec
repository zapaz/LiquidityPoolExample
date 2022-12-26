methods
{
    deposit(uint256)                        returns(uint256)
    assetBalance()                          returns(uint256) envfree
}

rule integrityOfDeposit {

    mathint balance_before = assetBalance();

    env e; uint256 amount;
    require e.msg.sender != currentContract;
    deposit(e, amount);

    mathint balance_after = assetBalance();

    assert balance_after == balance_before + amount,
        "deposit must increase the underlying balance of the pool";
}