(defun length-with-reduce (the-list)
  (reduce #'(lambda (x y) (+ x 1)) the-list :initial-value 0))  ; it is the more efficient solution given
