;; p. 114

(defvar *state* nil "current-state: list of conditions")
(defvar *ops* nil "available operators")
(defstruct op "an operation"
           (action nil) (preconds nil) (add-list nil) (del-list nil))

(defun gps (state goals &optional (*ops* *ops*))
  ;; (if (every #'achieve goals) 'solved))
  (remove-if #'atom (achieve-all (cons '(start) state) goals nil)))

(defun achieve (goal)
  "a goal is achieved if it already holds or there is an appropriate op for it"
  (or (member goal *state*)
      (some #'apply-op
            (find-all goal *ops* :test #'appropriate-p))))

(defun achieve-all (goals)
  (and (every #'achieve goals) (subsetp goals *state*)))

(defun appropriate-p (goal op)
  (member goal (op-add-list op)))

(defun apply-op (op)
  (when (achieve-all (op-preconds op))
    (print (list 'executing (op-action op)))
    (setf *state* (set-difference *state* (op-del-list op)))
    (setf *state* (union *state* (op-add-list op)))
    t))

(defun executing-p (x)
  (starts-with x 'executing))

(defun starts-with (list x)
  (and (consp list) (eql (first list) x)))

(defun convert-op (op)
  (unless (some #'executing-p (op-add-list op))
    (push (list 'executing (op-action op)) (op-add-list op)))
  op)

(defun op (action &key preconds add-list del-list)
  (convert-op
   (make-op :action action :preconds preconds
            :add-list add-list :del-list del-list)))

(defparameter *school-ops*
  (list
   (make-op :action 'ask-phone-number
            :preconds '(in-communication-with-shop)
            :add-list '(know-phone-number))
   (make-op :action 'drive-son-to-school
            :preconds '(son-at-home car-works)
            :add-list '(son-at-school)
            :del-list '(son-at-home))
   (make-op :action 'shop-installs-battery
            :preconds '(car-needs-battery shop-knows-problem shop-has-money)
            :add-list '(car-works))
   (make-op :action 'tell-shop-problem
            :preconds '(in-communication-with-shop)
            :add-list '(shop-knows-problem))
   (make-op :action 'telephone-shop
            :preconds '(know-phone-number)
            :add-list '(in-communication-with-shop))
   (make-op :action 'look-up-number
            :preconds '(have-phone-book)
            :add-list '(know-phone-number))
   (make-op :action 'give-shop-money
            :preconds '(have-money)
            :add-list '(shop-has-money)
            :del-list '(have-money))))

(mapc #'convert-op *school-ops*)
