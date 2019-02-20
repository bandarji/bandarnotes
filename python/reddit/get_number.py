while True:
    try:
        a = float(input('Number: '))
    except ValueError:
        print('Please, numbers only.')
        continue
    break
print('You entered a number: {}'.format(a))
