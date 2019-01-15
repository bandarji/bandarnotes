def ask(msg):
    return raw_input('{} '.format(msg))[0].lower()

def game_fight():
    print('Great! Meet Beta.')
    response = ask('Shake hands? [y/n]')
    if response in 'sy':
        print('** SHOCKED ** Ouch!')
        game_win()
    else:
        print('Let us try this again...')
        start_game()

def game_gohome():
    print('What if the Wright brothers only thought birds should fly?')
    print('Game over.\nSCORE: 0')

def game_win():
    print('Death blossom worked! You win!\nSCORE: 1000000000000000000000000000')

def start_game():
    print('Greetings starfighter. You have been recruited...')
    msg = 'Want to defend the frontier against Zur and the Kodan armada? [y/n] '
    response = ask(msg)
    if response in 'sy':
        game_fight()
    else:
        game_gohome()

def main():
    start_game()

if __name__ == '__main__':
    main()
