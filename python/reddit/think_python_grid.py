def grid():
    delimiter_row = ('{}{}'.format('+ ', '- ' * 4) * 4) + '+'
    openspace_row = ('{}{}'.format('|', ' ' * 9) * 4) + '|'
    for box_row in range(4 * 4):
        if box_row % 4 == 0:
            print(delimiter_row)
            print(openspace_row)
        else:
            print(openspace_row)
    print(delimiter_row)

grid()
