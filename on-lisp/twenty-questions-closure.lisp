(defvar *nodes* (make-hash-table))

(defun defnode (name conts &optional yes no)
  (setf (gethash name *nodes*)
        (if yes
            #'(lambda ()
                (format t "~a~%>> " conts)
                (case (read)
                  (y (funcall (gethash yes *nodes*)))
                  (t (funcall (gethash no *nodes*)))))
            #'(lambda () conts))))

(defnode 'creature "is the person a human?" 'human 'hybrid)
(defnode 'hybrid "is the person female?" 'female 'male)
(defnode 'female "is she a mage?" 'mage 'hybridmuggle)
(defnode 'mage "can she wield swords?" 'magicknight 'plainmage)
(defnode 'magicknight "is she a main character?" 'maincharacter 'sidecharacter)
(defnode 'maincharacter 'tina-branford)

(defnode 'human "is she a magician?" 'humanmage 'humanmuggle)
(defnode 'humanmage 'hermione-granger)

;; to start:
;; (funcall (gethash 'creature *nodes*))
