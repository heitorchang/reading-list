(define (fact n)
  (cond ((zero? n) 1)
        (#t (* n (fact (- n 1))))))

(define (fact2 n r)
  (cond ((zero? n) r)
        (#t (fact2 (- n 1) (* r n)))))

(define (fact3 n)
  (letrec
      ((fact2 (lambda (n r)
                (cond ((zero? n) r)
                      (#t (fact2 (- n 1) (* r n)))))))
    (fact2 n 1)))
