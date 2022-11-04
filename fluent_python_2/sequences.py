'''
Container sequences can hold items (references to objects it contains) of different types:
list, tuple, collections.deque

Flat sequences hold items (in their own memory space) of one simple type:
str, bytes, array.array

Mutable sequences:
list, bytearray, array.array, collections.deque

Immutable sequences:
str, bytes, tuple

Cartesian product with listcomp

tshirts = [(color, size) for size in sizes
                         for color in colors]

Genexps use the same syntax as listcomps, but are enclosed in parentheses instead of square brackets.
If the genexp is the single argument to a function call, it is not necessary to double the parentheses.

Tuples can be used as records (meaning is determined by the position of an item)

_ is conventionally used as a dummy variable's name, for an item that is not of interest (when unpacking a tuple, for example)

Tuples are of fixed length and their references cannot be deleted or replaced. However, if the object referred to is mutable, the tuple cannot prevent its modification.

Methods found in list and tuple (tuple does not allow modifying its size or contents)
__add__, __iadd__, append, clear, __contains__, copy, count, __delitem__, extend, __getitem__, __getnewargs__, index, insert, __iter__, __len__, __mul__, __imul__, __rmul__, pop, remove, reverse, __reversed__, __setitem__, sort
