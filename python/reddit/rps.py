import random

choices = ('rock', 'paper', 'scissors')
human_pick = raw_input('Choose (r)ock, (p)aper or (s)cissors: ').lower()[0]
comp_pick = random.choice(choices)[0]

game = human_pick + comp_pick
if human_pick not in 'rps':
    print('You did not choose a valid play.')
elif human_pick == comp_pick:
    print('Tied.')
elif game in ('rs', 'pr', 'sp'):
    print('The human won.')
else:
    print('The computer won.')
