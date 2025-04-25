# Write your MySQL query statement below
SELECT id FROM(
SELECT id, recordDate, temperature, LAG(recordDate) OVER (ORDER BY recordDate ASC) AS r2, LAG(temperature) OVER (ORDER BY recordDate ASC) AS t2
FROM Weather
ORDER BY recordDate ASC ) A 
WHERE A.temperature > A.t2
AND DATEDIFF(A.recordDate,A.r2)=1
