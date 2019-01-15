#!/usr/bin/env python

def ask_for_miles():
    while True:
        try:
            miles = float(input('How many miles? '))
        except ValueError as error:
            print('Error: {}'.format(error))
        else:
            return miles

def miles_to_kilometers(miles):
    return miles * 1.60934

def main():
    miles = ask_for_miles()
    kilometers = miles_to_kilometers(miles)
    print('{:0.4f} miles == {:0.4f} kilometers'.format(miles, kilometers))

if __name__ == '__main__':
    main()
