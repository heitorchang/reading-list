(defun interp (x &optional env)
  (cond
    ((symbolp x) (get-var x env))
    ((atom x) x)
    ((case (first x)
       (quote (second x))
       (begin (last1 (mapcar #'(lambda (y) (interp y env))
                             (rest x))))
       (set! (set-var! (second x) (interp (third x) env) env))
       (if (if (interp (second x) env)
               (interp (third x) env)
               (interp (fourth x) env)))
       (lambda (let ((parms (second x))
                     (code (maybe-add 'begin (rest2 x))))
                 #'(lambda (&rest args)
                     (interp code (extend-env parms args env)))))
       (t (apply (interp (first x) env)
                 (mapcar #'(lambda (v) (interp v env))
                         (rest x))))))))

(defun set-var! (var val env)
  (if (assoc var env)
      (setf (second (assoc var env)) val)
      (set-global-var! var val))
  val)

(defun get-var (var env)
  (if (assoc var env)
      (second (assoc var env))
      (get-global-var var)))

(defun set-global-var! (var val)
  (setf (get var 'global-val) val))

(defun get-global-var (var)
  (let* ((default "unbound")
         (val (get var 'global-val default)))
    (if (eq val default)
        (error "Unbound variable: ~a" var)
        val)))

(defun extend-env (vars vals env)
  (nconc (mapcar #'list vars vals) env))

(defparameter *scheme-procs*
  '(+ * < not)) ;; also: if, lambda

(defun init-scheme-interp ()
  (mapc #'init-scheme-proc *scheme-procs*)
  (set-global-var! t t)
  (set-global-var! nil nil))

(defun init-scheme-proc (f)
  (if (listp f)
      (set-global-var! (first f) (symbol-function (second f)))
      (set-global-var! f (symbol-function f))))

(defun maybe-add (op exps &optional if-nil)
  (cond ((null exps) if-nil)
        ((length=1 exps) (first exps))
        (t (cons op exps))))

(defun length=1 (x)
  (and (consp x) (null (cdr x))))

(defun rest2 (x) (rest (rest x)))

(defun last1 (list)
  (first (last list)))

(defun eval-in-scheme (input-string)
  (init-scheme-interp)
  (format nil "~a" (interp (read-from-string input-string))))

(defun solution (input)
  (eval-in-scheme input))
