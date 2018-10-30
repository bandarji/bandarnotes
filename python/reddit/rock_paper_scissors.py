#!/usr/bin/env python

import random

def display_winner(computer, player):
    outcomes = {
        (1, 2): 'Your paper covered the robot rock',
        (1, 3): 'Robot rocks smashed your scissors',
        (2, 1): 'Robot papers your rock for the win',
        (2, 3): 'You cut up the robot paperwork',
        (3, 1): 'Humans win: rock breaks scissors',
        (3, 2): 'Robot scissors cut through your paper',
    }
    play = (computer, player)
    return outcomes.get(play, "It's a draw")


def play_game():
    computer = random.randint(1, 3)
    player = player_choice()
    if player > 0:
        print(display_winner(computer, player))
    return player


def player_choice():
    choices = {
        'r': 1, # rock
        'p': 2, # paper
        's': 3, # scissors
    }
    invalid_choice = True
    while invalid_choice:
        choice = raw_input('Pick (r)ock, (p)aper, (s)cissors or (q)uit: ')
        if choice.lower() in 'rpsq':
            invalid_choice = False
            choice = choices.get(choice, 0) # otherwise 0 for quit
    return choice


def main():
    play_again = True
    while play_again:
        play_again = play_game()
    print('Thanks for playing...')


if __name__ == '__main__':
  main()
