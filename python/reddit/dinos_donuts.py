def take_order(menu):
    print('MENU\n====\n\n')
    for i, menu_item in sorted(menu.items()):
        print('{:<2} {:<15} {:0.2f}'.format(i, menu_item.get('item', ''),
                                            menu_item.get('cost', 0)))
    return raw_input('Select number to order or (q)uit: ')

def ring_up_customer(orders, menu_items):
    total = 0
    menu = {x.get('item'): x.get('cost') for x in menu_items}
    print('ORDER\n=====\n\n')
    for item, count in sorted(orders.items(), key=lambda r: 0 - r[1]):
        item_cost = menu.get(item)
        subtotal = count * item_cost
        total += subtotal
        print('{:<15} {} x {:0.2f} = {:0.2f}'.format(item, count, item_cost,
                                                     subtotal))
    print('Total: {:0.2f}'.format(total))

def main():
    menu = {
        1: {'item': 'puff', 'cost': 3.50},
        2: {'item': 'twizzler', 'cost': 2.25},
        3: {'item': 'strudel', 'cost': 4.05},
        4: {'item': 'dutchie', 'cost': 1.99},
    }
    not_done = True
    orders = {}
    while not_done:
        order = take_order(menu)
        if order.lower().startswith('q'):
            ring_up_customer(orders, menu.values())
            not_done = False
        else:
            choice = menu.get(int(order), {})
            if choice:
                item = choice.get('item')
                if item in orders:
                    orders[item] += 1
                else:
                    orders[item] = 1

main()
