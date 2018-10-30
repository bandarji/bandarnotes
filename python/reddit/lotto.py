import random

def lottery(winning_nums):
    tickets = set()
    attempt = 0
    num_count = len(winning_nums)
    won = False
    status = 'lost'
    ticket = []
    rejections = 0
    while not won:
        ticket = tuple(sorted([random.randint(1, 30) for _ in range(num_count)]))
        if ticket == tuple(winning_nums):
            status = 'won'
            won = True
        elif ticket in tickets:
            rejections += 1
        else:
            attempt += 1
            tickets.add(ticket)
        print('Attempt: {:10} {} {} r: {}'.format(attempt, ticket, status, rejections))

lottery(sorted([5, 15, 25]))
