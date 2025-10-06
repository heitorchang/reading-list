(setf *random-state* (make-random-state t))

(defun sentence () (append (noun-phrase) (verb-phrase)))
(defun noun-phrase () (append (Article) (Adj*) (Noun) (PP*)))
(defun PP () (append (Prep) (noun-phrase)))
(defun verb-phrase () (append (Verb) (noun-phrase)))
(defun Article () (one-of '(the a)))
(defun Noun () (one-of '(dude chick taco chair)))
(defun Verb () (one-of '(ate took bought liked)))
(defun Adj () (one-of '(big tiny blue red)))
(defun Prep () (one-of '(to in by with on)))

(defun Adj* ()
  (if (= (random 2) 0)
      nil
      (append (Adj) (Adj*))))

(defun PP* ()
  (if (= (random 2) 0)
      nil
      (append (PP) (PP*))))

(defun one-of (set)
  (list (random-elt set)))

(defun random-elt (choices)
  (elt choices (random (length choices))))
