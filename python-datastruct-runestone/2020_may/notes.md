# Python Data Structures

[Problem Solving with Algorithms and Data Structures using Python](https://runestone.academy/runestone/books/published/pythonds/index.html)


## 1.9 Input and output

`input(prompt)` displays the prompt and returns a string.

Interpreting the user's input as another type requires a type conversion.

```
sradius = input("Please enter the radius: ")
radius = float(sradius)
diameter = 2 * radius
```

## 1.13 Object-Oriented Programming (Classes)

```
class MyFraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom


    def __str__(self):
        return str(self.num) + "/" + str(self.den)
```

## 2.1 A proper Python class

For a class to be comparable, at the minimum, `__eq__` and `__lt__` must be implemented.

