(defpackage :match
  (:use :cl))

(in-package :match)

(defun variablep (sym)
  "Check if the first character of sym is ?"
  (char= #\? (char (symbol-name sym) 0)))

(defun match-element (e1 e2)
  "Return T if its two arguments are eql or if either is a variable (tested with variablep)."
  (and
   (symbolp e1)
   (symbolp e2)
   (or
    (eql e1 e2)
    (or (variablep e1) (variablep e2)))))
