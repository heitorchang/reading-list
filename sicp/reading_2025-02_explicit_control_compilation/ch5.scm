;; Chapter 5, p. 666

;; 668

(define (gcd a b)
  (if (= b 0)
      a
      (gcd b (remainder a b))))

;; 5.1.1, p. 672

;; A specification of the GCD machine, p. 673
;; quotes added by me
'(data-paths
  (registers
   ((name a)
    (buttons ((name a<-b) (source (register b)))))
   ((name b)
    (buttons ((name b<-t) (source (register t)))))
   ((name t)
    (buttons ((name t<-r) (source (operation rem))))))
  (operations
   ((name rem) (inputs (register a) (register b)))
   ((name =) (inputs (register b) (constant 0)))))
'(controller
 test-b
 (test =)
 (branch (label gcd-done))
 (t<-r)
 (a<-b)
 (b<-t)
 (goto (label test-b))
 gcd-done)

;; p. 675 alternative description
'(controller
  test-b
  (test (op =) (reg b) (const 0))
  (branch (label gcd-done))
  (assign t (op rem) (reg a) (reg b))
  (assign a (reg b))
  (assign b (reg t))
  (goto (label test-b))
  gcd-done)

;; gcd-machine.scm, p. 697

;; machine.scm, The Machine Model, p. 698
