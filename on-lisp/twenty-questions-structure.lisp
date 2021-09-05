;; structure for nodes

(defstruct node contents yes no)

(defvar *nodes* (make-hash-table))

(defun defnode (name conts &optional yes no)
  (setf (gethash name *nodes*)
        (make-node :contents conts
                   :yes yes
                   :no no)))

(defnode 'people "is the person a man?" 'male 'female)
(defnode 'male "is he living?" 'liveman 'deadman)
(defnode 'deadman "was he american?" 'us 'them)
(defnode 'us "is he on a coin?" 'coin 'cidence)
(defnode 'coin "is the coin a penny?" 'penny 'coins)
(defnode 'penny 'lincoln)

(defun run-node (name)
  "Type y for yes."
  (let ((n (gethash name *nodes*)))
    (cond ((node-yes n)
           (format t "~a~%>> " (node-contents n))
           (case (read)
             (y (run-node (node-yes n)))
             (t (run-node (node-no n)))))
          (t (node-contents n)))))

