import random
import time

def roshambo():
    return random.choice(('rock', 'paper', 'scissors'))

def report(wins, cycles):
    rock = wins['rock']
    paper = wins['paper']
    scissors = wins['scissors']
    draw = wins['draw']
    computer = wins['computer']
    human = wins['human']
    messages = [
        'Wins: (Someone won {:0.2f} percent of the cycles)'.format((cycles - draw) * 100.0 / cycles),
        '    Rock: {} ({:0.2f} percent)'.format(rock, rock * 100.0 / cycles),
        '    Paper: {} ({:0.2f} percent)'.format(paper, paper * 100.0 / cycles),
        '    Scissors: {} ({:0.2f} percent)'.format(scissors, scissors * 100.0 / cycles),
        'No one won {:0.2f} percent of the time'.format(draw * 100.0 / cycles),
        'Computer won {:0.2f} percent of the time'.format(computer * 100.0 / cycles),
        'Human won {:0.2f} percent of the time'.format(human * 100.0 / cycles),
    ]
    print('\n'.join(messages))

def rps_simulation(cycles):
    wins = {
        'draw': 0,
        'computer': 0,
        'human': 0,
        'rock': 0,
        'paper': 0,
        'scissors': 0,
    }
    for _ in range(cycles):
        game = (roshambo(), roshambo()) # (computer, human)
        if game[0] == game[1]:
            wins['draw'] += 1
        elif game in (('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')):
            wins['computer'] += 1
            wins[game[0]] += 1
        else:
            wins['human'] += 1
            wins[game[0]] += 1
    report(wins, cycles)

def main():
    start = time.time()
    cycles = 1000000
    rps_simulation(cycles)
    msg = 'Simulation of {} cycles ran for {:0.3f} seconds'
    print(msg.format(cycles, time.time() - start))

if __name__ == '__main__':
    main()
