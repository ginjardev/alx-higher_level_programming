-- lists the number of records with the same score in the table second_table
SELECT score, count(score) as number
FROM second_table
GROUP By score
ORDER BY score DESC; 

