SELECT 
	*,
	CONCAT(first_name," ",last_name) AS full_name
FROM 
	class_demo.users
    ;

INSERT INTO
	users
    (first_name, last_name, email)
VALUES
	("Barney", "Rubble", "barney@badrock.com"),
	("BamBam", "Flintstone", "bambam@badrock.com")
    ;

UPDATE
	class_demo.users
SET 
	first_name="Fred" 
WHERE
	id=2
    ;


DELETE FROM
	users
    
WHERE
	id=2
;

/* 1-many relationship */
SELECT 
	* 
FROM 
	class_demo.cars /* child table */

LEFT JOIN users ON users.id = cars.user_id /* users is parent */

WHERE
	users.id=4
;

/* many-many relationship */
SELECT
	*
FROM
	users /* left table */
    
LEFT JOIN user_like_car ON user_like_car.user_id = users.id /* middle table */
LEFT JOIN cars ON cars.id = user_like_car.car_id /* right table */

;

/* many-to-many relationship going the other way */
SELECT
	*
FROM
	cars /* left table */
    
JOIN user_like_car ON user_like_car.car_id = cars.id /* middle table */
JOIN users ON users.id = user_like_car.user_id /* right table */

;