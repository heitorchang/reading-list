<html>
<body>

Use &lt;?php tags throughout to generate PHP results

https://www.php.net/manual/en/language.basic-syntax.phpmode.php

Tags: only use <?php ?> and <?= ?> to maximize compatibility.


https://www.php.net/manual/en/language.types.string.php

<pre>
Heredoc = <<<EOT

acts like a double-quoted string
...
EOT;

Nowdoc = <<<'EOT'

acts like a single-quoted string
...
EOT;


class people {
  public $john = "John smith";
  public $jane = "Jane smith";
}

$p = new people();

echo "$p->john";

</pre>

String indices may be negative.

<pre>
$s = 'string';
$s[-2] => 'n'
</pre>

complex (curly) syntax is {$square->width}

individual characters in a string may be modified with $str[42] = "x"

https://www.php.net/manual/en/language.types.array.php

`unset($arr[5]);` removes the element from the array
`unset($arr);` removes the whole array

`$array = array_values($array);` re-indexes the array (resets integer indices to start from 0)

https://www.php.net/manual/en/language.types.object.php

a new object is created by instantiating a class with the `new` statement

```
class foo {
  function do_something() {
    echo "foo";
  }
}

$bar = new foo;
```

a generic object may be created with `$obj = new stdClass();`

check for NULL with `is_null()`

