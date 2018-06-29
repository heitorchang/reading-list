<?php
// run php -S 127.0.0.1:8000
// then go to http://127.0.0.1:8000/printable_notes.php

$NOTES_FILE = "notes4_2018_jun.txt"

?>
<head>
    <style>
     @font-face {
         font-family: 'Inconsolata';
         src: url('Inconsolata-Regular.ttf') format('truetype');
         font-style: normal;
     }

     pre {
         font-family: 'Inconsolata';
         line-height: 88%;
         white-space: pre-wrap;
     }
    </style>
</head>
<body>
    <pre>
<?php include($NOTES_FILE); ?>
    </pre>
</body>
