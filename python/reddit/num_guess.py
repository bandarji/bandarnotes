import random

def guess_a_number(turn_number, guesses):
    guessed_number = 0
    guess_invalid = True
    while guess_invalid:
        prompt = '[Turn {}] Enter number between 1 and 20: '.format(turn_number)
        try:
            guessed_number = int(input(prompt))
        except ValueError:
            print('Invalid. Try again.')
        if guessed_number in guesses:
            continue
        if 1 <= guessed_number <= 20:
            guesses.add(guessed_number)
            guess_invalid = False
    return guessed_number, guesses

def main():
    computer_number = random.randint(1, 20)
    turn_number = 1
    guesses = set()
    game_message = 'You lost because you ran out of turns.'
    while turn_number <= 5:
        guessed_number, guesses = guess_a_number(turn_number, guesses)
        if guessed_number == computer_number:
            game_message = 'You won on turn {}'.format(turn_number)
            break
        turn_number += 1
    print(game_message)

main()
