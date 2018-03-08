# https://www.reddit.com/r/learnpython/comments/82ucgu/calling_an_input_inside_a_def_function/

def main():
    while True:
        word = raw_input('Enter a word: ')
        if word == '-1':
            break
        not_ = '' if word[:] == word[::-1] else ' not'
        print "Word '%s' is%s a palindrome" % (word, not_)

main()
