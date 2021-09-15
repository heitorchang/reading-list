;; 1.7

(defun mappend (fn the-list)
  "Apply fn to each element of list and append the results."
  (apply #'append (mapcar fn the-list)))

(defun self-and-double (x) (list x (+ x x)))

;; (mappend #'self-and-double '(1 20 300))

(defun mappend-build (fn the-list)
  (if (null the-list)
      nil
      (append (funcall fn (first the-list))
              (mappend-build fn (rest the-list)))))

;; ex. 1.2
(defun power (base pow)
  (if (= pow 0)
      1
      (* base (power base (- pow 1)))))
