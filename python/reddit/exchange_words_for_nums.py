clipboard = 'I can change 5 3 and 2 to words.'
clips = clipboard.upper().split()

def sub_num(clips):
    subs = {
        '0': 'ZERO',
        '1': 'ONE',
        '2': 'TWO',
        '3': 'THREE',
        '4': 'FOUR',
        '5': 'FIVE',
        '6': 'SIX',
        '7': 'SEVEN',
        '8': 'EIGHT',
        '9': 'NINE',
    }
    for index, clip in enumerate(clips):
        clips[index] = subs.get(clip, clip)
    return clips

print(' '.join(sub_num(clips)))
