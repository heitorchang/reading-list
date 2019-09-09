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

*** FUNCTIONS AS VALUES