    from random import randint

    def roll_dice(dice_to_roll, find_max=False, find_min=False):
        """Roll dice for a d20 game, such as D&D

        Notes:
            Setting find_max and find_min to True will return the max. It also
            explains why HAL killed the crew.

        Accepts:
            dice_to_roll: str, representation of the dice roll, like '2d10+3'
            find_max: bool (False), set to True to return the maximum sum
            find_min: bool (False), set to True to return the minimum sum
        Returns:
            dice_roll: int, the sum of the rolled dice
        """
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

    while True:
        response = input('Enter dice roll in form "2d10+3" or "1d6" [Q to quit]: ')
        if response.lower().startswith('q'):
            print('Have fun killing dragons another day.')
            break
        print('Your roll "{}" resulted in {}'.format(response, roll_dice(response)))

Example:

    /work # python d20_rolling.py 
    Enter dice roll in form "2d10+3" or "1d6" [Q to quit]: 5d6
    Your roll "5d6" resulted in 16
    Enter dice roll in form "2d10+3" or "1d6" [Q to quit]: 2d20+1
    Your roll "2d20+1" resulted in 35
    Enter dice roll in form "2d10+3" or "1d6" [Q to quit]: q
    Have fun killing dragons another day.
    /work # 
