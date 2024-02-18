-- Displaus the average temperature (in F) by city by descending oreder.
SELECT city, AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;