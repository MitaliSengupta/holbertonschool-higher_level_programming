-- script that displays the max temp of each stqate ordered by state name
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state LIMIT 3
