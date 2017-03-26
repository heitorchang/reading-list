def lunch_orders():
    q("""SELECT s.name AS student_name, m.name AS menu_name, m.price
    FROM my_purchase AS p
    INNER JOIN my_student AS s
    ON p.student_id = s.id
    INNER JOIN my_lunchmenu AS m
    ON p.menu_item = m.id
    ORDER BY student_name""")

def lunch_totals_by_student():
    q("""SELECT s.name AS student_name, SUM(m.price) AS total
    FROM my_purchase AS p
    INNER JOIN my_student AS s
    ON p.student_id = s.id
    INNER JOIN my_lunchmenu AS m
    ON p.menu_item = m.id
    GROUP BY student_name
    ORDER BY student_name""")

def lunch_totals_by_menu_item():
    q("""SELECT m.name AS menu_name, COUNT(*) AS ct, SUM(m.price) AS total
    FROM my_purchase AS p
    INNER JOIN my_student AS s
    ON p.student_id = s.id
    INNER JOIN my_lunchmenu AS m
    ON p.menu_item = m.id
    GROUP BY menu_name
    ORDER BY menu_name""")
