(defpackage :little-schemer
  (:use :cl))

(in-package :little-schemer)

(defun null? (x) (null x))
(defun zero? (x) (= x 0))

;; (atom '()) is T, while the text expects it to be NIL
(defun atom? (x)
  (not (listp x)))

(defun list? (x) (listp x))

(defun add1 (x) (+ x 1))
(defun sub1 (x) (- x 1))

(defun eq? (x y) (equal x y))
