from random import randint

def roll_dice(dice_to_roll, find_max=False, find_min=False):
    times = 0
    sides = 0
    additional = 0
    if '+' in dice_to_roll:
        additional = int(dice_to_roll.split('+')[1])
        times, sides = dice_to_roll.split('d')
        times = int(times)
        sides = int(sides.split('+')[0])
    else:
        times, sides = dice_to_roll.split('d')
        times = int(times)
        sides = int(sides)
    if find_max:
        dice_roll = (times * sides) + additional
    elif find_min:
        dice_roll = times + additional
    else:
        dice_roll = sum([randint(1, sides) for _ in range(times)]) + additional
    return dice_roll

def display_history(dice_to_roll, repeat=1000, graph_width=80):
    history = {}
    floor = roll_dice(dice_to_roll, find_min=True)
    ceiling = roll_dice(dice_to_roll, find_max=True)
    for i in range(repeat):
        dice_roll = roll_dice(dice_to_roll)
        history[dice_roll] = history.get(dice_roll, 0) + 1
    rolls_high = max(history.values())
    x_unit = int((rolls_high * 1.05) // graph_width)
    for i in range(1, ceiling + 1):
        rolls = history.get(i, 0)
        print('{:4} {}'.format(i, '#' * (rolls // x_unit)))

def main():
    display_history('2d8', repeat=50000, graph_width=30)

main()
