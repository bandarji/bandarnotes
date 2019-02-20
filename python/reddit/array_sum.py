def problem2(numbers):
    number_count = len(numbers)
    if number_count % 2 == 0:
        response = sum([number for number in numbers if isinstance(number, int) or isinstance(number, float)])
    else:
        response = [number_count for number in numbers]
    return response

tests = [
    [],
    [0],
    [1],
    [3, 5],
    [3, 5, 7],
    [3, 5, 7, "nine"],
]

for test in tests:
    print(test, problem2(test))
