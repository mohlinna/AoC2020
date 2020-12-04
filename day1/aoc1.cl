(defun get-file (filename)
  (with-open-file (stream filename)
    (loop for line = (read-line stream nil)
          while line
          collect line)))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
"Part 1"
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defun find_2020 (x y remaining_x remaining_y)
	(if (= 2020 (+ x y))
		(* x y)
		(if remaining_y
			(find_2020 x (car remaining_y) remaining_x (cdr remaining_y))
			(find_2020 (car remaining_x) (cadr remaining_x) (cdr remaining_x) (cddr remaining_x)))))

(defun find_2020_from_list (inputs)
	(find_2020 (car inputs) (cadr inputs) (cdr inputs) (cddr inputs)))

(defun find_my_2020 ()
	(find_2020_from_list (map 'list (lambda (x) (parse-integer x)) (get-file "input.txt"))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
"Part 2"
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(defun find_2020_3 (x y z remaining_x remaining_y remaining_z)
	(if (= 2020 (+ x y z))
		(* x y z)
		(if remaining_z
			(find_2020_3 x y (car remaining_z) remaining_x remaining_y (cdr remaining_z))
			(if (> (list-length remaining_y) 1)
				(find_2020_3 x (car remaining_y) (cadr remaining_y) remaining_x (cdr remaining_y) (cddr remaining_y))
				(find_2020_3 (car remaining_x) (cadr remaining_x) (caddr remaining_x) (cdr remaining_x) (cddr remaining_x) (cdddr remaining_x))))))

(defun find_2020_3_from_list (inputs)
	(find_2020_3 (car inputs) (cadr inputs) (caddr inputs) (cdr inputs) (cddr inputs) (cdddr inputs)))

(defun find_my_2020_3 ()
	(find_2020_3_from_list (map 'list (lambda (x) (parse-integer x)) (get-file "input.txt"))))
