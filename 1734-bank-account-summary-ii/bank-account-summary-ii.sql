/* Write your T-SQL query statement below */

SELECT C.name , D.balance FROM
Users C
INNER JOIN (
SELECT A.account,SUM(B.amount) AS balance
FROM Users A 
INNER JOIN Transactions B ON
A.account = B.account 
GROUP BY A.account HAVING SUM(amount) > 10000) D 
ON C.account = D.account