def test():
    pass

# p. 30, French deck of cards

from collections import namedtuple

# Verbose name cannot have spaces; must be valid identifier
Card = namedtuple('Card_verbose_name_displayed_on_print', 'rank suit')

# p. 31 select a random element

from random import choice

print("Random from [0, 1]: ", choice([0, 1]))

