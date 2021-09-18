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

(defun random-elt (choices)
  (elt choices (random (length choices))))

;; ex. 2.4
(defun cross-product (fn xlist ylist)
  (mappend #'(lambda (y)
               (mapcar #'(lambda (x) (funcall fn x y)) xlist))
           ylist))

(defun find-all (item sequence &rest keyword-args
                 &key (test #'eql) test-not &allow-other-keys)
  (if test-not
      (apply #'remove item sequence
             :test-not (complement test-not) keyword-args)
      (apply #'remove item sequence
             :test (complement test) keyword-args)))

(setf (symbol-function 'find-all-if) #'remove-if-not)

;; p. 124

(defvar *dbg-ids* nil)

(defun dbg (id format-string &rest args)
  (when (member id *dbg-ids*)
    (fresh-line *debug-io*)
    (apply #'format *debug-io* format-string args)))

(defun ai-debug (&rest ids)
  (setf *dbg-ids* (union ids *dbg-ids*)))

(defun ai-undebug (&rest ids)
  (setf *dbg-ids* (if (null ids) nil
                      (set-difference *dbg-ids* ids))))

(defun dbg-indent (id indent format-string &rest args)
  (when (member id *dbg-ids*)
    (fresh-line *debug-io*)
    (dotimes (i indent) (princ "  " *debug-io*))
    (apply #'format *debug-io* format-string args)))
