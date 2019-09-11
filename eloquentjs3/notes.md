# 01 Values, types, and operators

Special numbers

Infinity, -Infinity, NaN

`Number.isNaN()` checks for NaN

Strings

* `backtick-quoted strings are template literals`
* 'single quotes'
* "double quotes"

a backslash is an "escape character" that "escapes" the character after it, giving it a special meaning

${} in template literals compute its contents, converts it to a string and includes it in that position

typeof 4.5

Usually, null and undefined are interchangeable

use === and !== to bypass type conversions

# 02 Program structure

the simplest kind of statement is an expression with a semicolon after it.

the keyword `let` defines a binding

`let one = 1, two = 2`


`var` should be avoided because it has some confusing properties. Use `let` instead

`const` points at the same value for as long as it lives.

`prompt` function may be used in experiments

* `Number()` converts a value to a number.
* `String()` converts to a string
* `Boolean()` converts to a Boolean

`if (!Number.isNaN(n)) { ... }` translates to "unless `n` is NaN, do this".

```
if (...) {
  ...
} else if (...) {
  ...
} else {
  ...
}
```

```
let yourName;

do {
  yourName = prompt("who are you?");
} while (!yourName);
```

do loops always execute their bodies at least once

`for (let initializer; check; update state) { ... }`

`break` exits the loop. `continue` jumps back to the beginning of the loop and continues with its next iteration

```
switch (prompt("what is the weather like?")) {
  case "rainy":
    // take an umbrella
    break;
  case "sunny":
    // dress lightly
  case "cloudy":
    // go outside
    break;
  default:
    // unknown weather type
    break;
}
```

# 03 Functions

```
const square = function(x) {
  return x * x;
};
```

`let` and `const` are local to the block they are declared in.

in pre-2015 JS, only functions created new scopes. `var` bindings are visible throughout the whole function that they appear in

lexical scoping is a convention where scope is determined by the place of that variable in the program text. Each local scope can see all the local scopes that contain it, and so on.

```
let someFunctionName = function() {
  ...
};
```

allows you to use the name in arbitrary expressions, not just call it. It can be passed as an argument to another function.

```
function square(x) {
  ...
}
```

is a function declaration. The definition is moved to the top of its scope.

```
const power = (base, exponent) => {
  ...
};
```

is an example of an arrow function.

The arrow comes after the list of parameters and is followed by the function's body

with only one parameter, the parentheses (forming the parameter list) are optional

if the body is a single expression, braces should be omitted, and that expression will be returned from the function

```
const square1 = (x) => { return x * x; };
const square2 = x => x * x;
```

are the same thing

```
function chicken() {
  return egg();
}
function egg() {
  return chicken();
}
console.log(chicken() + " came first");
// stack overflow
```

## Optional arguments

`function power(base, exponent = 2) { ... }` sets the default value of `exponent` to `2`

## Closure

The ability to reference a specific instance of a local binding in an enclosing scope is *closure*. A function that references bindings from local scopes around it is *a* closure.

It is as if a function value contains both the code in their body and the environment in which it was created.

```
function multiplier(factor) {
  return number => number * factor;
}
```

`var` bindings end up in the nearest function scope or the global scope.

# 04 Data Structures: Objects and arrays

Numbers, strings and Booleans are the atoms that data structures are built from

an array stores sequences of values

`array[index]` retrieves the numbered element (starting from 0) from the array

using a dot or brackets accesses a property, such as `item.x`. With `item[x]`, `x` is evaluated first

elements in an array are stored as the array's properties, using numbers as property names

both string and array objects contain properties that hold function values, such as `s.toUpperCase()`.

properties that contain functions are usually called *methods* (such as `toUpperCase` is a method of a string).

`Array.push(value)` and `Array.pop()`

## Objects

Values of the type *object* are arbitrary collections of properties.

```
let day = {
  squirrel: false,
  events: ["work", "tree", "pizza"]
};
```

properties whose names aren't valid binding names have to be quoted

`delete obj.prop` removes the property, but it is not common

`"prop" in obj` checks if the property is present in `obj`

`Object.keys(someObj)` returns an array of strings of its property names

`Object.assign(target, ...sources)` copies properties from `sources` to `target`. It may be used to create shallow copies.

https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/assign

```
let obj = {a: 1};
let copy = Object.assign({}, obj);
```

One way to deep clone is to use `JSON.parse(JSON.stringify(obj1))`

## Mutability

numbers, strings and Booleans are *immutable*. you can derive values from them, but their values will remain the same.

However, objects' properties can be changed. objects are references to values and other objects

you may have two or more references to the same object, or two objects that contain the same properties. `obj1 == obj2` will check if their *identity* is the same

There is no built-in operation to compare two objects' contents.

```
function addEntry(events, squirrel) {
  journal.push({events, squirrel});
}
```

When a property name in brace notation isn't followed by a value, it's taken from the binding with the same name (`events: events`)

Arrays have an `includes` method that checks whether a given value exists in the array.

`events.includes(event)`

## Array loops

the old way

```
for (let i = 0; i < JOURNAL.length; i++) {
  let entry = JOURNAL[i];
  // do something with entry
}
```

can be done now as

```
for (let entry of JOURNAL) {
  // do something
}
```

`for (aChar of aString) { ... }` iterates over the string.

## Further Arrayology

in addition to `push` and `pop`, there are `unshift(elem)` to add and `shift()` to remove at the start of an array

the `indexOf(item)` method looks for `item` starting from the left. `lastIndexOf(item)` starts at the end. An optional second argument indicates where to start searching

`slice` takes a start index (inclusive) and an optional end index (exclusive). There is no step parameter like in Python. If `slice()` is called, a shallow copy is made.

`concat(otherArray)` glues arrays together

## Strings and their properties

Although strings, numbers and Booleans have built-in properties and methods, you cannot store custom properties in them

`"one two three".indexOf("ee")` can be used to search a multi-character string, while the array's `indexOf` can only be used to look for a single element

`trim()` removes whitespace from either end of a string.

`padStart(length, character)` left pads a string

`split(separator)` and `array.join(str)` converts between strings and arrays

`aString.repeat(times)` repeats `aString`

## Rest Parameters

to write a function that accepts a variable amount of arguments, put three dots before the function's last parameter: `function max(...numbers) { ... }`

the *rest parameter* is bound to an array

```
let numbers = [3, 4, 9];
max(...numbers)
```

three dots are also used to call a function with an array of arguments (spreading)

`max(9, ...numbers, 2)` is also allowed

```
let words = ["banana", "a"];
console.log(["a", ...words, "pear"]);
```

though JavaScript warns you if you redeclare a variable with `let` or `const`, you won't be warned when overwriting standard bindings

`Math.PI` is written in all caps because of the convention of writing constants in all caps

`Math.random()` returns a value between zero (inclusive) and one (exclusive)

`Math.floor(Math.random() * 10)` returns an integer from 0 to 9 inclusive.

```
function phi([n00, n01, n10, n11]) {
  ...
}
```

instead of `function phi(table)` is an example of destructuring

Destructuring also works for objects

```
let {name} = {name: "Fred", age: 23};
console.log(name);
```

## JSON

*Serializing* is converting objects in memory into a flat description

JSON (JavaScript Object Notation) is a popular format

`JSON.stringify` and `JSON.parse` are used to convert data to and from this format

a (linked) list is different from an array:

```
let list = {
  value: 1,
  rest: {
    value: 2,
    rest: {
      value: 3,
      rest: null
    }
  }
};
```

To test if something is a real object, use `typeof x == "object" && x != null`

# Higher-order functions

the array method `forEach` provides a `for/of` loop as a higher-order function

`["A", "B"].forEach(e => console.log(e));`

** 86/98 script data set