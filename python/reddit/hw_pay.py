def ask(msg, number=True):
    """Return valid user response to a question.

    Accepts:
        msg, str: What to display to the user
        number, bool: Whether to enforce entry of a number
    Returns:
        response, (str|float): User entry, either string or float
    """
    while True:
        response = input('{}: '.format(msg))
        if number:
            try:
                test = float(response)
            except ValueError:
                pass
            else:
                return float(response)
        else:
            return response

def calc_pay(sales, hours, rate_comm=0.05, rate_hourly=7.5, rate_wh=25.0):
    comm = sales * rate_comm
    gross = hours * rate_hourly + sales * rate_comm
    taxes = gross * (rate_wh / 100.0)
    net = gross - taxes
    return {
        'sales': sales,
        'hours': hours,
        'comm': comm,
        'gross': gross,
        'taxes': taxes,
        'net': net,
    }

def pay_stub(name, pay_info):
    comm = pay_info.get('comm', 0.0)
    gross = pay_info.get('gross', 0.0)
    taxes = pay_info.get('taxes', 0.0)
    net = pay_info.get('net', 0.0)
    hours = pay_info.get('hours', 0.0)
    sales = pay_info.get('sales', 0.0)
    row_header = '{:<30}{:>8}{:>8}{:>8}{:>8}{:>8}{:>8}'
    row_data = '{:<30}{:>8.2f}{:>8.2f}{:>8.2f}{:>8.2f}{:>8.2f}{:>8.2f}'
    print(row_header.format('NAME', 'GROSS', 'NET', 'TAXES', 'HOURS', 'SALES', 'COMM'))
    print('=' * (30 + 8 + 8 + 8 + 8 + 8 + 8))
    print(row_data.format(name, gross, net, taxes, hours, sales, comm))

def main():
    name = ask('Enter employee name', number=False)
    sales = ask('Enter sales amount')
    hours = ask('Enter hours worked')
    pay_info = calc_pay(sales, hours, rate_comm=0.07, rate_wh=30.0)
    pay_stub(name, pay_info)

main()


$ py37a python /work/hw_pay.py 
Enter employee name: Samantha Howell
Enter sales amount: 5590
Enter hours worked: 21
NAME                             GROSS     NET   TAXES   HOURS   SALES    COMM
==============================================================================
Samantha Howell                 548.80  384.16  164.64   21.00 5590.00  391.30
