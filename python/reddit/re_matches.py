import re

def valid_phone(phone):
    valid = False
    matches = [
        re.match(r'^01[0-9]{3}\ [0-9]{6}$', phone),
        re.match(r'^01[0-9]1\ [0-9]{3}\ [0-9]{4}$', phone),
        re.match(r'^11[0-9]\ [0-9]{3}\ [0-9]{4}$', phone),
        re.match(r'^02[0-9]\ [0-9]{4}\ [0-9]{4}$', phone),
    ]
    if any(matches):
        valid = True
    return valid

def run_tests():
    tests = [
        {'phone': '01333 789121', 'expected': True},
        {'phone': '01333a789121', 'expected': False},
        {'phone': '41333 789121', 'expected': False},
        {'phone': '01333 7891217', 'expected': False},
        {'phone': '0171 333 4444', 'expected': True},
        {'phone': '01711 333 4444', 'expected': False},
        {'phone': '0171 333 44441', 'expected': False},
        {'phone': '111 333 4444', 'expected': True},
        {'phone': '111 333 44441', 'expected': False},
        {'phone': '029 4444 4444', 'expected': True},
        {'phone': '029 4444 44441', 'expected': False},
        {'phone': '029 4444.4444', 'expected': False},
    ]
    for test in tests:
        phone = test.get('phone')
        expected = test.get('expected')
        print('{:15} Valid/Expected: {} / {}'.format(phone,
                                                     valid_phone(phone),
                                                     expected))

def main():
    run_tests()

main()
