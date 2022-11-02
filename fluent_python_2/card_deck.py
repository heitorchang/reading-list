'''
Ex. 1-1

Implements just two special methods, __getitem__ and __len__

'''

import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'clubs diamonds hearts spades'.split()

    def __init__(self):
        self._cards = [Card(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # Needed to shuffle, shown in Ch. 13
    # def __setitem__(self, ...):


def spades_high(card):
    """Used to sort the deck."""
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def hearts_high(card):
    """Used to sort the deck."""
    suit_values = dict(spades=2, hearts=3, diamonds=1, clubs=0)
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

'''
deck = FrenchDeck()

from random import choice

choice(deck)
#> Card(rank='5', suit='diamonds')

for card in sorted(deck, key=hearts_high):
    print(card)

'''
