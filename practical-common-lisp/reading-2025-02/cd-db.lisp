(defvar *db* nil)
(defparameter *db-filename* (pathname "~/reading-list/practical-common-lisp/reading-2025-02/cds.db"))

(defun make-cd (title artist rating ripped)
  (list :title title :artist artist :rating rating :ripped ripped))

(defun add-record (cd) (push cd *db*))

(defun dump-db ()
  (dolist (cd *db*)
    (format t "~{~a:~10t~a~%~}~%" cd)))

(defun prompt-read (prompt)
  (format *query-io* "~a: " prompt)
  (force-output *query-io*)
  (read-line *query-io*))

(defun prompt-for-cd ()
  (make-cd
   (prompt-read "Title")
   (prompt-read "Artist")
   (or (parse-integer (prompt-read "Rating") :junk-allowed t) 0)
   (y-or-n-p "Ripped")))

(defun add-cds ()
  (loop (add-record (prompt-for-cd))
        (if (not (y-or-n-p "Another?")) (return))))

(defun clear-db ()
  (setf *db* nil))

(defun save-db ()
  "Save *db* to *db-filename*"
  (with-open-file (out *db-filename*
                       :direction :output
                       :if-exists :supersede)
    (with-standard-io-syntax
      (print *db* out))))

(defun load-db ()
  (with-open-file (in *db-filename*)
    (with-standard-io-syntax
      (setf *db* (read in)))))
