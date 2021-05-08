;; initial definition
;;
;; (define (sqrt-iter guess x)
;;   (if (good-enough? guess x)
;;       (* guess 1.0)
;;       (sqrt-iter (improve guess x) x)))

;; (define (improve guess x)
;;   (average guess (/ x guess)))

;; (define (average x y)
;;   (/ (+ x y) 2))

;; (define (good-enough? guess x)
;;   (< (abs (- (square guess) x)) 0.000001))

;; (define (my-sqrt x)
;;   (sqrt-iter 1.23 x))


;; block structure

(define (my-sqrt x)
  (define (sq-iter g)
    (if (g-good g)
        (* g 1.0)
        (sq-iter (imp g))))

  (define (imp g)
    (avg g (/ x g)))

  (define (avg x y)
    (/ (+ x y) 2))

  (define (g-good g)
    (< (abs (- (square g) x)) 0.00001))

  (sq-iter 1))
       
