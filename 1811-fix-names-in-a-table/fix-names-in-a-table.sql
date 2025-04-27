/* Write your T-SQL query statement below */
SELECT A.user_id, CONCAT(UPPER(substring(A.name,1,1)),substring(A.name,2,len(A.name))) AS name
FROM (SELECT user_id, LOWER(name) AS name
FROM Users) A ORDER BY A.user_id