#!/usr/bin/env python

def calc_months(total, interest_rate, monthly_spend):
    months = 0
    balance = total
    while months < 600 and balance > 0:
        months += 1 # go one month
        balance -= monthly_spend # remove monthly spend from balance
        balance += balance * (interest_rate / 1200.0) # add monthly interest
    return months

def main():
    print(calc_months(300000, 6, 3000))
    print(calc_months(10000, 0, 2000))
    print(calc_months(1000000, 4.5, 4200))
    print(format(calc_months(1000000, 4.6, 4200), '.2f'))

if __name__ == '__main__':
    main()
    