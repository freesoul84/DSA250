# Write your MySQL query statement below
/*
SELECT MAX(A.num) AS num
FROM (SELECT num 
FROM MyNumbers 
GROUP BY num 
HAVING COUNT(num) = 1) A
*/

SELECT COALESCE((SELECT num 
FROM MyNumbers
GROUP BY num
HAVING COUNT(num) =1
ORDER BY num DESC
LIMIT 1),null)
AS num