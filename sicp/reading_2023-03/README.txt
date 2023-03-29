Using Windows

Installed Racket and set up Emacs to load Racket.exe:

(setq scheme-program-name "C:/Progra~1/Racket/Racket.exe -I r5rs")

Racket functions (such as andmap) are not accessible

However, the reader behaves as in Racket:

(1 . < . 2) => #t
