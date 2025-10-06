;; Rule-based solution

(load "/home/heitor/code/reading-list/paradigms-of-ai/book-code.lisp")
(setf *random-state* (make-random-state t))

(defparameter *simple-grammar*
  '((sentence -> (noun-phrase verb-phrase))
    (noun-phrase -> (Article Noun))
    (verb-phrase -> (Verb noun-phrase))
    (Article -> the a)
    (Noun -> man ball woman table)
    (Verb -> hit took saw liked))
  "A grammar for English")

;; 2.5
(defparameter *bigger-grammar*
  '((sentence -> (noun-phrase verb-phrase))
    (noun-phrase -> (Article Adj* Noun PP*) (Name) (Pronoun))
    (verb-phrase -> (Verb noun-phrase PP*))
    (PP* -> () (PP PP*))
    (Adj* -> () (Adj Adj*))
    (PP -> (Prep noun-phrase))
    (Prep -> to in by with on)
    (Adj -> big little blue green)
    (Article -> the a)
    (Name -> Tina Alice Jim Lee Robin)
    (Noun -> man ball woman table)
    (Pronoun -> he she it these those that)
    (Verb -> hit took saw liked))
  "A grammar for English")

(defvar *grammar* *bigger-grammar*
  "The grammar used by generate")

(defun rule-lhs (rule)
  (first rule))

(defun rule-rhs (rule)
  (rest (rest rule)))

(defun rewrites (category)
  (rule-rhs (assoc category *grammar*)))

(defun generate (phrase)
  (cond ((listp phrase)
         (mappend #'generate phrase))
        ((rewrites phrase)
         (generate (random-elt (rewrites phrase))))
        (t (list phrase))))

(defun generate-alt (phrase)
  "Alternative way of generate"
  (if (listp phrase)
      (mappend #'generate-alt phrase)
      (let ((choices (rewrites phrase)))
        (if (null choices)
            (list phrase)
            (generate-alt (random-elt choices))))))

(defun generate-tree (phrase)
  (cond ((listp phrase)
         (mapcar #'generate-tree phrase))
        ((rewrites phrase)
         (cons phrase
               (generate-tree (random-elt (rewrites phrase)))))
        (t (list phrase))))

(defun generate-all (phrase)
  "Does not work with bigger-grammar because of recursive definitions.
First, evaluate
(setf *grammar* *simple-grammar*)
"
  (cond ((null phrase) (list nil))
        ((listp phrase)
         (combine-all (generate-all (first phrase))
                      (generate-all (rest phrase))))
        ((rewrites phrase)
         (mappend #'generate-all (rewrites phrase)))
        (t (list (list phrase)))))

(defun combine-all (xlist ylist)
  (mappend #'(lambda (y)
               (mapcar #'(lambda (x) (append x y)) xlist))
           ylist))
