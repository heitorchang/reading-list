(defpackage :calculator
  (:use :cl))

(in-package :calculator)

(defun combine-expr (operator operand expr-list)
  "Return the expression with the operator and operand applied to the first member of the expression."
  (cons
   (list operand operator (first expr-list))
   (rest expr-list)))
