def bills_needed(money):
    """Determine optimal numbers of each bill denomination for amount.

    Args:
        money, int: Amount of money to figure bills for
    Returns:
        cash, dict: Count of each type of bill needed for sum
    """
    denominations = [1, 2, 5, 10, 20, 50, 100]
    cash = {}
    balance = money
    bill_count = 0
    if money > 0:
        for denomination in sorted(denominations, reverse=True):
            bills = balance // denomination
            if bills > 0:
                cash[denomination] = bills
                bill_count += bills
                balance = balance % denomination
    return bill_count, cash

def test_bills_needed():
    tests = [
        1,
        2,
        42,
        51,
        123,
        222,
        500,
    ]
    for test in tests:
        bill_count, cash = bills_needed(test)
        print('Money: {}, Bills: {} - {}'.format(test, bill_count, cash))

def main():
    test_bills_needed()

main()
