(defpackage :sicp-cl
  (:use :cl)
  (:shadow :gcd))

;; Evaluate this in the REPL
;; (in-package :sicp-cl)

;; p. 63

(defun gcd (a b)
  (if (= b 0)
      a
      (gcd b (rem a b))))
