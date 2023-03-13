(defpackage :util
  (:use :cl))

(in-package :util)

(defun elementp (obj)
  "Return T if obj is a number, symbol, character, or package."
  (or
   (numberp obj) (symbolp obj) (characterp obj) (packagep obj)))

(export 'elementp)
