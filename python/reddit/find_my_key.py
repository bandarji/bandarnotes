def find_key(info, key):
    value = -1
    if isinstance(info, dict):
        if key in info:
            print('Found {} in {}'.format(key, info))
            return info.get(key)
        else:
            for element in info:
                print('Testing element {}'.format(element))
                value = find_key(info.get(element), key)
                if value != -1:
                    return value
    return value

def main():
    tests = [
        {
            'a': 1,
            'e': 5,
        },
        {
            'a': 1,
            'b': 2,
            'c': {'d': 4, 'e': 5},
            'f': 6,
        },
        {
            'a': 1,
            'b': 2,
        },
    ]
    for test in tests:
        print('Test: {}, Value for e: {}'.format(test, find_key(test, 'e')))

main()
