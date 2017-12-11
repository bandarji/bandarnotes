def rate():
    # OP complained that the input compares were not working
    # if x == [7, 10]
    # I mentioned that the input is a string and the range compares were wrong
    try:
        x = int(raw_input('Rate service from 1 to 10: '))
    except ValueError:
        raise SystemExit('Enter a number between 1 and 10')
    if x >= 7 and x <= 10: print('Thanks!')
    elif x >= 4 and x < 7: print('Thank you.')
    elif x >= 1 and x < 4: print('Crap.')
    else: print('Enter a number between 1 and 10')
