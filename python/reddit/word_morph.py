#!/usr/bin/env python3

"""
Morph from one word to another
./word_morph.py <word_file> <start_word> <end_word>
"""

import sys

def find(start, end, words, max_length=5):
    """Discover all word paths. Path cannot exceed max_length elements.
    Args:
        start: str or list, starting word or generated path
        end: str, the ending word
        words: set, the set of all words
        max_length: stop processing if the word path grows beyond this count
    Yields:
        path: list
    """
    if not isinstance(start, list):
        start = [start]
    if len(start) < max_length:
        for path in nextpath(start, words):
            if path[-1] == end:
                yield path
            for path in find(path, end, words, max_length):
                yield path

def pull_words(words_file, word_length):
    """Compile set of words, converted to lower case and matching length of
    start and end words.
    Args:
        words_file: str, name of the file containing all words
        word_length: int, length of the start/end words
    Returns:
        words_set: set, all possible interesting words
    """
    words_set = set()
    with open(words_file) as words:
        for word in words:
            word_ = word.strip().lower()
            if len(word_) == word_length and word_ not in words_set:
                words_set.add(word_)
    return words_set

def distance_one(possible, word):
    """Checks if the number of characters changed between two words is one.
    Args:
        possible: str, possibly the next word
        word: str, real path word to test against
    Returns:
        bool, True if one letter distance
    """
    difference = 0
    for i, _ in enumerate(possible):
        if difference > 1:
            return False
        if possible[i] != word[i]:
            difference += 1
    return difference == 1

def neighborhood(word, words):
    """Finds words within the word set which are one letter distance from
    current word in a path.
    Args:
        word: str, current word in a path
        words: set, the set of all words
    Yields:
        possible: str, possible next word
    """
    for possible in words:
        if distance_one(possible, word):
            # print('Next neighbor word: {}'.format(possible))
            yield possible

def nextpath(path, words):
    """Generate list of possible paths.
    Args:
        path: list, current path of words
        words: set, full set of words (remove words already in path)
    Yields:
        path + [word]: list, add found word to the current path
    """
    words = set(words) - set(path)
    for word in neighborhood(path[-1], words):
        # print('Next neighbour path: {}'.format(path + [word]))
        yield path + [word]

def flight_check():
    """Ensures proper command line arguments set and words will work.
    Returns:
        (
            words: set, all words
            start_word: str, starting word
            end_word: str, ending word
        )
    """
    if len(sys.argv) != 4:
        error_msg = 'Usage: {} <word_file> <word1> <word2>'.format(sys.argv[0])
        raise SystemExit(error_msg)
    start_word = sys.argv[2].lower()
    end_word = sys.argv[3].lower()
    word_length = len(start_word)
    if len(end_word) != word_length:
        error_msg = ('Words not of same length: '
                     '{} / {}'.format(start_word, end_word))
        raise SystemExit(error_msg)
    words = pull_words(sys.argv[1], word_length)
    if start_word not in words or end_word not in words:
        error_msg = 'Words not in dictionary'
        raise SystemExit(error_msg)
    return words, start_word, end_word

def display_results(paths_count, paths):
    """Show discovered paths
    Args:
        paths_count: int, number of paths discovered
        paths: list of list, word chains found
    """
    key_func = lambda x: len(x)
    if paths_count == 1:
        print('Path: {}'.format(paths[0]))
    elif paths_count > 1:
        print('{:10} {}'.format('Shortest:', min(paths, key=key_func)))
        print('{:10} {}'.format('Longest:', max(paths, key=key_func)))
    else:
        print('No paths discovered')

def main():
    """Main function"""
    words, start_word, end_word = flight_check()
    paths = list(find(start_word, end_word, words, max_length=5))
    display_results(len(paths), paths)

if __name__ == '__main__':
    main()
