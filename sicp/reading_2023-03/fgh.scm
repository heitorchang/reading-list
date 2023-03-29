;; use in the REPL to trace and untrace:
;; ,tr g
;; ,untr g

(define (f x) (+ 1 x))

(define (g x) (/ 1 x))

(define (h x) (- (f x) (g x)))
