import random
temperatures = [(_, random.randint(-10, 10)) for _ in range(100)] # some data
longest_period = 0
current_period = 0
for i, temp_data in enumerate(temperatures):
    date, temperature = temp_data # tuple of (date, temperature)
    if i == 0:
        continue # basically skip the first temperature because we will compare
                 # against the prior temp to see if we're still negative
    # Compare the temperature at the current position with the one before it
    # If both are negative, then increase the current cold period by one
    # If not, then see if this period exceeds the previous longest cold period
    # Then, reset the current cold period
    if temperatures[i - 1][1] < 0 and temperatures[i][1] < 0:
        current_period += 1
    else:
        longest_period = current_period if current_period > longest_period else longest_period
        if current_period > 0:
            print('Cold lasted {} cycles, ended on {}'.format(current_period, date))
        current_period = 0
print('Longest cold period: {} cycles'.format(longest_period))
