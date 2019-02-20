    #!/usr/bin/env python

    import random

    def display_dice(dice):
        print('\nHere are your current dice rolls:\n')
        row = '{:>10} {:>10}' # Generate columnar output
        print(row.format('DIE NUMBER', 'DIE VALUE'))
        print(row.format('=' * 10, '=' * 10))
        for die, roll in enumerate(dice):
            print(row.format(die, roll))
        print('TOTAL: {}'.format(sum(dice)))

    def roll_die():
        return random.randint(1, 6)

    def main():
        dice = []
        while True:
            if not dice:
                # no dice rolled yet
                print('Howdy. Now, we roll five dice.')
                dice = [roll_die() for _ in range(5)] # gen a list of the dice rolls
            display_dice(dice) # show our current state of dice rolls
            response = input('Dice to reroll [Q to quit]: ') # get user response
            if response.lower().startswith('q'):
                # user wants to quit
                print('Thanks. Exiting.')
                break # exits the while loop
            for die in [int(i) for i in response.split() if i in '01234']:
                # for each number entered in, reroll the die at that index
                dice[die] = roll_die()

    if __name__ == '__main__':
        main()

Example:

    /work # ./five_dice.py 
    Howdy. Now, we roll five dice.

    Here are your current dice rolls:

    DIE NUMBER  DIE VALUE
    ========== ==========
             0          1
             1          6
             2          1
             3          1
             4          6
    TOTAL: 15
    Dice to reroll [Q to quit]: 0

    Here are your current dice rolls:

    DIE NUMBER  DIE VALUE
    ========== ==========
             0          4
             1          6
             2          1
             3          1
             4          6
    TOTAL: 18
    Dice to reroll [Q to quit]: q
    Thanks. Exiting.
