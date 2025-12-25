from app.calculation import add, sub, mul, BankAccount
import pytest

## Adding pytest decorator fixture for  testing to minimize the repetative tasks
@pytest.fixture
def zero_bank_account():
    print("Creating empty bank account")
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)


##Adding a decorator for mutiple test case for a specific fucntion
@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (7, 1, 8),
    (12, 4, 16)
])
## Writing test function for add
def test_add(num1, num2, expected):
    print("Testing add function")
    # assert add(5, 3) == 8
    # assert add(1, 1) == 2
    # assert add(-1, 1) == 0
    ## decorator use kore kortesi
    assert add(num1, num2) == expected


    

def test_sub():
    assert sub(5, 3) == 2
    assert sub(4, 1) == 3
    assert sub(10, 20) == -10

def test_mul():
    assert mul(5, 3) == 15
    assert mul(10, 10) == 100
    assert mul(5, 0) == 0

### Testing Bankaccout class funtion
# def test_bank_set_inital_ammount():
#     x= BankAccount(50)
#     assert x.balance==50

### This test_bank by using fixture decorator
def test_bank_set_inital_ammount(bank_account):
    assert bank_account.balance==50

# def test_bank_default_ammount():
#     x= BankAccount()
#     assert x.balance==0
def test_bank_default_ammount(zero_bank_account):
    assert zero_bank_account.balance==0

def test_deposit(bank_account):
    # x=BankAccount(50)
    # x.deposit(50)
    # assert x.balance==100
    bank_account.deposit(50)
    assert bank_account.balance==100


def test_withdraw(bank_account):
    # x=BankAccount(200)
    # x.withdraw(100)
    # assert x.balance==100
    bank_account.withdraw(50)
    assert bank_account.balance==0


def test_collect_interest(bank_account):
    # x=BankAccount(100)
    # x.collect_interest()
    # assert round(x.balance,6)==110
    bank_account.collect_interest()
    assert round(bank_account.balance,6)==55


@pytest.mark.parametrize("deposited, withdrew, expected", [
    (200, 100, 100),
    (50, 10, 40),
    (1200, 200, 1000)
])

def test_bank_transaction(zero_bank_account, deposited, withdrew, expected):
    zero_bank_account.deposit(deposited)
    zero_bank_account.withdraw(withdrew)
    assert zero_bank_account.balance==expected


def test_insufficient_funds(bank_account):
    with pytest.raises(ValueError):
        bank_account.withdraw(200)
    