(defun length10 (list)
  (length10-aux list 0))

(defun length10-aux (sublist len-so-far)
  (if (null sublist)
      len-so-far
      (length10-aux (rest sublist) (+ 1 len-so-far))))
  
(defun length12 (the-list)
  (labels
      ((length13 (list len-so-far)
         (if (null list)
             len-so-far
             (length13 (rest list) (+ 1 len-so-far)))))
    (length13 the-list 0)))
