'''
Ch. 1

Python Data Model

Special method names are always written with leading and trailing double underscores (dunder methods).

obj[key] is supported by __getitem__.

Other uses:

Collections
Attribute access
Iteration
Operator overloading
Function and method invocation
String representation and formatting
Asynchronous programming using await
Object creation and destruction
Managed contexts (with, async/await)
'''


'''
len(my_object) accesses a C struct called PyVarObject, which contains an ob_size field holding the number of items in the collection.

Reading this field is much faster than calling a method.
'''


'''
Special methods allow:

emulating numeric types
creating string representations of objects
defining the Boolean value of an object
implementing collections
'''


'''
Fig. 1-2

Interfaces of the essential collection types

Iterable: __iter__
Sized: __len__
Container: __contains__
Reversible: __reversed__
Collection: (nothing)

Sequence: for list, str
Mapping: for dict, defaultdict
Set: for set, frozenset

'''
