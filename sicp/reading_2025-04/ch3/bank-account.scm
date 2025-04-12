;; p. 302

;; message-passing style

(define (make-account balance)
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds"))
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)
  (define (dispatch message)
    (cond ((eq? message 'withdraw) withdraw)
          ((eq? message 'deposit) deposit)
          (else (error "Unknown request: make-account" m))))
  dispatch)

(define my-acct (make-account 0))
((my-acct 'deposit) 1000)
