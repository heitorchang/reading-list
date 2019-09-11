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

# 05 Higher-order functions

the array method `forEach` provides a `for/of` loop as a higher-order function

`["A", "B"].forEach(e => console.log(e));`

`filter` is an array method that keeps values that passes a test

`WRITING_SCRIPTS.filter(s => s.direction == "ttb")`

`map` applies a function to elements of an array

`rtlScripts.map(s => s.name);`

`[1, 2, 3].map(x => x * 100);`

`reduce` builds a value by repeatedly taking a single element from the array and combining it with the current value

`[1, 2, 3, 4].reduce((a, b) => a + b, 0)`

`some(test)` is a method that returns true if one or more elements satisfies the given test

`all(test)` tests if all elements pass the test

## Emojis

`let horseShoe = "HS"` (pretend H and S are emojis)

`horseShoe.length` -> `4`
`horseShoe[0]` -> <?>
`horseShoe.codePointAt(0)` -> 128052

To count the number of characters, use `[...s].length`

`findIndex` finds the first value for which the given function returns true. It returns `-1` if no such element is found

flatten an array of arrays (but no deeper)

```
  function flatten(a) {
    return a.reduce((result, e) => result.concat(e), []);
  }
```

# 06 The secret life of Objects

Object-oriented programming divides programs into smaller pieces and make each piece responsible for managing its own state (local state)

Interaction between objects is done through *interfaces*

Properties may be public or private

*Encapsulation* is separating the interface from the implementation

Methods are properties that hold functions

the binding called `this` in a method points at the object that it was called on

```
function speak(line) {
  console.log(`The ${this.type} rabbit says ${line}`);
}
```

to pass `this` explicitly, use the function's `call` method, which takes the `this` value as its first argument and treats further arguments as normal parameters.

`speak.call(hungryRabbit, "Burp!")`

A function has its own `this` binding, so you cannot refer to the `this` of the wrapping scope in a function defined with the `function` keyword.

On the other hand, arrow functions do not bind their own `this`. They use the `this` binding of their enclosing scope.

## Prototypes

a prototype is an object that is used as a fallback source of properties

an unsuccessful search for a property goes to its prototype, then the prototype's prototype, and so on.

`Object.prototype` is the object behind almost all objects. Its prototype is `null`.

There exist `Array.prototype` and `Function.prototype`

`Object.create(aPrototype)` will create an object with a specific prototype

## Classes

A *class* defines the shape of a type of object, the methods and properties it has. A specific object is called an *instance* of the class

Methods are shared in all instances, but properties that differ need to be stored individually in each instance

A *constructor* function defines the properties that instances are supposed to have.

by putting the `new` keyword in front of a function call, the function is treated as a constructor

by convention, constructor names are capitalized

```
function Rabbit(type) {
  this.type = type;
}
Rabbit.prototype.speak = function(line) {
  console.log(`The ${this.type} rabbit says ${line}`);
};

let weirdRabbit = new Rabbit("weird");
```

The new way is:

```
class Rabbit {
  constructor(type) {
    this.type = type;
  }
  speak(line) {
    console.log(`The ${this.type} rabbit says ${line}`);
  }
}

let killerRabbit = new Rabbit("killer");
```

several methods may be written inside the class declaration. `constructor` is treated as a special method

right now, there are no ways of adding properties to a class (only methods). The prototype has to be manipulated after defining the class

`class` may be used in an expression to produce the constructor as a value. A class name is not needed

```
let object = new class { getWord() { return "hello"; } };
console.log(object.getWord());
```

if there is a property in a prototype, adding a property to an object will hide the prototype's property.

`Rabbit.prototype.teeth = "small";` can be written to affect all rabbits. However, `killerRabbit.teeth = "long, sharp";` will only affect `killerRabbit`.

## Map data structure

A *map* associates values (keys) with other values. Objects may be used as maps

```
let ages = {
  Boris: 39,
  Liang: 22,
}
```

`${ages["Boris"]}` -> 39
`"Jack" in ages` -> false
`"toString" in ages` -> true

to avoid properties present in `Object.prototype`, a map can be created with `Object.create(null)`.

`new Map();` should be used instead of a regular object. it allows any type of keys

```
let ages = new Map();
ages.set("Boris", 39);
console.log(ages.get("Boris"));
```

`Object.keys` returns only an object's own keys, not those in the prototype.

as an alternative to the `in` operator, such as `"a" in obj`, `obj.hasOwnProperty("a")` will ignore the object's prototype.

## Polymorphism

`toString` may be overridden to produce a more useful result than `[object Object]`.

```
Rabbit.prototype.toString = function() {
  return `a ${this.type} rabbit`;
};
```

*Polymorphism* is a technique of writing code that works with dissimilar objects that have a certain interface. Polymorphic code works with values of different shapes, as long as they support the expected interface

** 107/119 symbols