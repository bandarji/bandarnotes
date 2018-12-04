def isprime(number):
    if number < 2:
        prime = False
    else:
        # The square root of the number, rounded up, is a valid final
        # check. The all() will return True if all division tests return
        # a remainder.
        highest_check = int(number ** 0.5 + 1)
        prime = all(number % i for i in range(2, highest_check))
    return prime

# print all primes between 0 and 100
for i in [x for x in range(101) if isprime(x)]:
    print(i)
