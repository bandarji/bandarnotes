def ask_for_nums():
    numbers = []
    while True:
        input_ = raw_input('Enter a number or (q)uit: ')
        if input_.lower().startswith('q'):
            break
        try:
            number = float(input_)
        except ValueError as err:
            print('Error: I do not believe "{}" is a number'.format(input_))
        else:
            numbers.append(number)
    return numbers

def numbers_avg(numbers):
    return (sum(numbers) * 1.0) / len(numbers)

numbers = ask_for_nums()
if numbers:
    average = numbers_avg(numbers)
    print('Average: {:>5.2} for {}'.format(average, numbers))
else:
    print('No average for an empty list')
