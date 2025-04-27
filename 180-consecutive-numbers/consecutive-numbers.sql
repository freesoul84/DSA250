/* Write your T-SQL query statement below */

SELECT DISTINCT num AS ConsecutiveNums
FROM (SELECT A.num, A.num1, LEAD(A.num1) OVER(order by A.id) AS num2
FROM (SELECT id,num, LEAD(num) OVER(order by id) AS num1
FROM Logs) A ) B WHERE B.num = B.num1 AND B.num1 = B.num2 AND B.num2 = B.num