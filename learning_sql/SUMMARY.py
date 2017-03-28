summary = """

CREATE TABLE person
(person_id SMALLINT UNSIGNED AUTO_INCREMENT,
 fname VARCHAR(32),
 birth_date DATE,
 CONSTRAINT pk_person PRIMARY KEY (person_id)
);

CREATE TABLE favorite_food
(person_id SMALLINT UNSIGNED,
 food VARCHAR(20),
 CONSTRAINT pk_favorite_food PRIMARY KEY (person_id, food),
 CONSTRAINT fk_fav_food_person_id FOREIGN KEY (person_id) REFERENCES person (person_id)
);

INSERT INTO person (fname, birth_date)
VALUES ('Tim', '1992-03-20');

INSERT INTO favorite_food (person_id, food)
VALUES (1, 'Hot dog');

"""
