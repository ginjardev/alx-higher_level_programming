-- ists all the cities of California that can be found in the database hbtn_0d_usa
USE hbtn_0d_usa;

SELECT c.id, c.name FROM cities c
WHERE c.state_id IN (
	SELECT s.id
	FROM states s
	WHERE s.name = "California"
)
ORDER BY c.id;