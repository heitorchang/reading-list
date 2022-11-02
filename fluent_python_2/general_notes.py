'''
__str__ uses __repr__ as a fallback, so prioritize implementing __repr__.

__bool__ and __len__, if defined, are used to determine the Boolean value of an instance of user-defined classes. If __len__ is defined and __len__(x) is 0, it is considered False.

Since Python 3.7, the insertion order of keys in a dict is preserved. However, you cannot rearrange the keys in a dict in any order you'd like.

'''
