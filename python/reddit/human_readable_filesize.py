def formatted_filesize(size):
    original_size = size
    units = ['bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB']
    highest_unit = units[-1]
    for i, unit in enumerate(units):
        if size < 1024:
            msg = '{} {}'.format(size, unit)
            break
        else:
            if unit == highest_unit:
                msg = '{} bytes'.format(original_size)
            size /= 1024
    return msg

tests = [
    0,
    1023,
    1023 + 60,
    10 * 1024 * 1024 * 1024,
    50 * 1024 * 1024 * 1024 * 1024,
    50 * 1024 * 1024 * 1024 * 1024,
    50 * 1024 * 1024 * 1024 * 10240,
    50 * 1024 * 1024 * 1024 * 1024000,
    50 * 1024 * 1024 * 1024 * 1024000000,
    50 * 1024 * 1024 * 1024 * 102400000000,
    50 * 1024 * 1024 * 1024 * 10240000000000,
    50 * 1024 * 1024 * 1024 * 1024000000000000,
]
for test in tests:
    print formatted_filesize(test)
