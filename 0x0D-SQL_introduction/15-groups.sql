-- This script lists the number of records with the same score in table `second_table`
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
GROUP BY score DESC;
