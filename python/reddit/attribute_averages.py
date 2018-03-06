def attribute_averages(sites):
    attributes = {}
    for site in sites:
        name = site.get('name')
        value = site.get('value')
        if name and value:
            if name in attributes:
                attributes[name]['count'] += 1
                attributes[name]['value'] += value
            else:
                attributes[name] = {'count': 1, 'value': value}
        else:
            raise SystemExit('WTF?')
    for attribute, value in attributes.items():
        count = value.get('count', 0)
        total = float(value.get('value', 0))
        if count > 0:
            print('Attribute {} averages {:.2f} ({} / {})'.
                  format(attribute, total / count, total, count))

attribute_averages(
    [
        {'url': 'example.com/example1', 'name': 'name1', 'value': 0.13},
        {'url': 'example.com/example1', 'name': 'name3', 'value': 0.14},
        {'url': 'example.com/example2', 'name': 'name1', 'value': 0.13},
        {'url': 'example.com/example3', 'name': 'name2', 'value': 0.43},
        {'url': 'example.com/example3', 'name': 'name3', 'value': 0.23},
    ]
)
