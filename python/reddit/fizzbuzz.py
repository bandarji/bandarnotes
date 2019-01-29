import sys

def fizz_buzz(ceiling):
    """Display numbers, replacing evenly-divisible numbers with fuzz/buzz.

    Starting with 1, show numbers up to and including the ceiling value. If the
    number is evenly divisible by 3, display "Fizz"; "Buzz" when evenly
    divisible by 5. When by both, display "FizzBuzz".

    Accepts:
        ceiling: int, Finally number to consider for display
    """
    # From 1 to the ceiling (+1 to include the ceiling number)
    for number in range(1, ceiling + 1):
        if number % 5 == 0 and number % 3 == 0:
            # If evenly divisible by both
            # the elif and else will not get considered when this is true
            sys.stdout.write("FizzBuzz ")
        elif number % 5 == 0:
            sys.stdout.write("Buzz ")
        elif number % 3 == 0:
            sys.stdout.write("Fizz ")
        else:
            sys.stdout.write('{} '.format(number))
    sys.stdout.flush()

def fizz_buzz2(ceiling):
    print ' '.join(
        'Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i)
        for i in  range(1, ceiling + 1)
    )

fizz_buzz(15)
print('')
fizz_buzz2(15)
