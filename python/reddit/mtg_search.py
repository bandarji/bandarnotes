#!/usr/bin/env python2.7

from pprint import pprint as pretty

def card_search(match_color, match_cost, match_text):
    cards = {
        'Force of Will':
            {
                'color': 'blue',
                'mana_cost': 5,
                'mana_string': '3UU',
                'description': 'Blah, blah, blah, counter target spell'
            },
        'Counterspell':
            {
                'color': 'blue',
                'mana_cost': 2,
                'mana_string': 'UU',
                'description': 'Blah, blah, blah, counter target spell'
            },
        'Misdirection':
            {
                'color': 'blue',
                'mana_cost': 5,
                'mana_string': '3UU',
                'description': 'Blah, blah, blah, target spell'
            }
    }
    matched_cards =\
    [
        card
        for card in cards.values()
        if (
            card.get('color', '') == match_color
            and card.get('mana_cost', 0) == match_cost
            and match_text in card.get('description', '')
        )
    ]
    return matched_cards

if __name__ == '__main__':
    cards = card_search('blue', 5, 'counter target spell')
    pretty(cards)
