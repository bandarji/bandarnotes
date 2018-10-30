#!/usr/bin/env python

# I've got a list data structure with (at most) several hundred entries,
# corresponding to variables in a statistical model being called into SAS from 
# a text file. What I would like to do is remove commented-out variables from my
# list, indicated by "/*" on the front end and "*/" on the back end.

# Example input list:

# ['inter', 'ca', 'ak', 'hi', 'or', 'qu1', 'qu2', 'qu3', 'pm1', 'pm2', 'pm3', '/*c', 'gq1', 'gq2*/', 'gq12']

# What I'd like my program to do is remove '/*c', 'gq1', 'gq2*/' from the above and leave me with the following "clean" list:

# ['inter', 'ca', 'ak', 'hi', 'or', 'qu1', 'qu2', 'qu3', 'pm1', 'pm2', 'pm3', 'gq12']

# From there, I just need to do a len() to get the number of elements remaining
# in the list. Note that there are multiple places in my file where the above
# occurs, so my program might need to do this up to dozens of times, not just
# once.

def strip_array(array):
    stripped_array = []
    start_found = False
    end_found = False
    for element in array:
        if isinstance(element, str) and element.startswith('/*'):
            start_found = True
        if isinstance(element, str) and element.endswith('*/'):
            start_found = False
            end_found = True
        if not start_found and not end_found:
            stripped_array.append(element)
    return stripped_array

def main():
    arrays = [
        ['inter', 'ca', 'ak', 'hi', 'or', 'qu1', 'qu2', 'qu3', 'pm1', 'pm2', 'pm3', '/*c', 'gq1', 'gq2*/', 'gq12'],
        [],
        [1, 3, 5, '/*start', None, 'friend', 'end*/'],
        ['/*', '*/'],
    ]
    for array in arrays:
        print('Original: {:5} {}'.format(len(array), array))
        stripped_array = strip_array(array)
        print('Stripped: {:5} {}\n'.format(len(stripped_array), stripped_array))

if __name__ == '__main__':
    main()
