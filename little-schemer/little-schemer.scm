;; For The Little Schemer

;; Preface: xii
(define atom?
  (lambda (x)
    (and (not (pair? x)) (not (null? x)))))

;; 16
(define lat?
  (lambda (l)
    (cond
     ((null? l) #t)
     ((atom? (car l)) (lat? (cdr l)))
     (else #f))))

;; 22
(define member?
  (lambda (a lat)
    (cond
     ((null? lat) #f)
     (else (or (eq? (car lat) a)
               (member? a (cdr lat)))))))

;; 41
(define rember
  (lambda (a lat)
    (cond
     ((null? lat) '())
     ((eq? (car lat) a) (cdr lat))
     (else (cons (car lat)
                 (rember a (cdr lat)))))))

;; 172
(define Y
  (lambda (le)
    ((lambda (f) (f f))
     (lambda (f)
       (le (lambda (x) ((f f) x)))))))

(define sketchy-fact
  (lambda (s)
    (lambda (a)
      (cond ((zero? a) 1)
            (else (* a (s (- a 1))))))))

;; ((Y sketchy-fact) 5) => 120
;; ((sketchy-fact (Y sketchy-fact)) 5) => 120
