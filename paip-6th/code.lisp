;;; p. 19
(defun mappend (fn the-list)
  "Apply fn to each element of list and append the results"
  (apply #'append (mapcar fn the-list)))

(defun double-in-list (x)
  (list (* x 2)))

(defun self-and-double (x) (list x (* x 2)))

;;; p. 20
(defun mappend-alternate (fn the-list)
  (if (null the-list)
      nil
      (append (funcall fn (first the-list))
              (mappend-alternate fn (rest the-list)))))

;;; p. 31 ex. 1.2
(defun power (base exp)
  (if (= exp 0)
      1
      (* base (power base (- exp 1)))))
