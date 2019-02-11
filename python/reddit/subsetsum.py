def subset_sum(numbers, count, total):
    """Determine if there exist a subset of elements which add up to a total.

    Accepts:
        numbers: list, array of values
        count: int, some number of elements
        total: int, sum for element_count to reach from array
    Returns:
        bool: whether numbers contains a subset of elements which add up to total
    """
    numbers.sort() # inefficient / should perform only once / meh
    candidates = [[]] # create a list of lists
    # Step through all numbers, keeping track of our index (i)
    for i, element in enumerate(numbers):
        possible = len(candidates)
        for k in range(possible + 1):
            possible = candidates[k] + [element] # possible combination
            candidates.append(possible) # add to our candidates of possible combos
            if sum(set(possible)) == total and len(set(possible)) == count:
                # aha! we found a combination with the right number of elements
                print('sum({}) == {}'.format(possible, total))
                return True
    # all combinations exhausted
    return False

tests = [
    {'numbers': [5, 3, 6, 11], 'count': 1, 'total': 3, 'answer': True},
    {'numbers': [5, 3, 6, 11], 'count': 1, 'total': 11, 'answer': True},
    {'numbers': [5, 3, 6, 11], 'count': 1, 'total': 7, 'answer': False},
    {'numbers': [5, 3, 6, 11], 'count': 2, 'total': 9, 'answer': True},
    {'numbers': [5, 3, 6, 11], 'count': 2, 'total': 10, 'answer': False},
    {'numbers': [5, 3, 6, 11], 'count': 3, 'total': 22, 'answer': True},
    {'numbers': [5, 3, 6, 11], 'count': 3, 'total': 23, 'answer': False},
    {'numbers': range(100, 300, 3) + [2, 5, 7, 10, 19, 8], 'count': 7, 'total': 827, 'answer': True},
]

for test in tests:
    numbers = test['numbers']
    count = test['count']
    total = test['total']
    answer = test['answer']
    print('\n{}'.format(test))
    if subset_sum(numbers, count, total) != answer:
        print('[TEST FAILED]')
    else:
        print('[TEST PASSED]')
