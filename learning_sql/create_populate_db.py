# INSERT, UPDATE, and DELETE needs cnx.commit()

# p. 20
create_sql = """CREATE DATABASE foreign_sales
CHARACTER SET utf8 COLLATE utf8_general_ci;"""

def now():
    print_simple_query(cnx, """
    SELECT now() AS now;
    """)

def create_person(cnx):
    cursor = cnx.cursor()
    cursor.execute("""
    CREATE TABLE person
    (person_id SMALLINT UNSIGNED,
    fname VARCHAR(32),
    lname VARCHAR(32),
    gender CHAR(1),
    birth_date DATE,
    CONSTRAINT pk_person PRIMARY KEY (person_id)
    );""")
    cursor.close()

def create_fav_food(cnx):
    cursor = cnx.cursor()
    cursor.execute("""
    CREATE TABLE favorite_food
    (person_id SMALLINT UNSIGNED,
    food VARCHAR(20),
    CONSTRAINT pk_favorite_food PRIMARY KEY (person_id, food),
    CONSTRAINT fk_fav_food_person_id FOREIGN KEY (person_id) REFERENCES person (person_id)
    )""")
    cursor.close()

def alter_auto_inc(cnx):
    # will not work if favorite_food exists because of foreign key constraint
    cursor = cnx.cursor()
    cursor.execute("""
    ALTER TABLE person MODIFY person_id SMALLINT UNSIGNED AUTO_INCREMENT;
    """)
    cursor.close()

drop_sql = "DROP TABLE favorite_food"

def insert_person(cnx, name, gender, bday):
    cursor = cnx.cursor()
    fname, lname = name.split()
    sql = """INSERT INTO person (fname, lname, gender, birth_date)
    VALUES (%s, %s, %s, %s);"""
    
    cursor.execute(sql, (fname, lname, gender, bday))
    cnx.commit()
    cursor.close()

def update_person(cnx):
    cursor = cnx.cursor()
    cursor.execute("""
    UPDATE person
    SET fname = 'Jimmy'
    WHERE person_id = 1;
    """)
    cnx.commit()
    cursor.close()

def delete_person(cnx):
    cursor = cnx.cursor()
    cursor.execute("""
    DELETE FROM person WHERE person_id > 1;
    """)
    cnx.commit()
    cursor.close()
