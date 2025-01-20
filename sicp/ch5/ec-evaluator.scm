;; 5.4

;; Stack + 7 registers:
;; exp: holds the expression to be evaluated
;; env: the environment in which the evaluation is to be performed
;; val: the value obtained by evaluating this expression
;; continue: for implementing recursion
;; proc, argl, unev: for evaluating combinations

;; eval-dispatch
