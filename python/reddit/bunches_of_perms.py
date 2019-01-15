import itertools

def main():
    all_words = set()
    test_word = 'dontaskmofoskatepunk'
    ceiling = len(test_word) + 1
    words = load_dictionary(ceiling)
    for i in range(2, ceiling):
        valid_words = None
        valid_words = check_word(words, test_word, i)
        if valid_words:
            all_words = all_words.union(valid_words)
        else:
            print('Stopped at {} chars, no more findings'.format(i))
            break
    print(all_words)



def load_dictionary(ceiling):
    with open('/usr/share/dict/words') as f:
        words = {w.lower().strip() for w in f if len(w) <= ceiling}
    return words


def check_word(words, letters, i):
    permutations = {''.join(p) for p in itertools.permutations(letters, i)}
    valid_words = {p for p in permutations if p in words}
    print(len(valid_words))
    return valid_words


main()
