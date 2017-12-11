#!/usr/bin/env python

def vowel_percent(in_str):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowel_count = 0
    consonant_count = 0
    total = 0
    for a_char in in_str:
        if a_char in vowels or a_char in consonants:
            total += 1 # only increment total for letters, not space/punctuation
            if a_char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    if total != 0: # don't want to divide by zero
        _vowel_percent = (100.0*vowel_count)/total
    else:
        _vowel_percent = 0.0
    print("Letters in string '{}' are {:.2f} percent vowels.".
          format(in_str, _vowel_percent))

def main():
    vowel_percent('The quick brown fox jumped over the lazy dog')
    vowel_percent('XYZ')

if __name__ == '__main__':
    main()
