/* Write your T-SQL query statement below */
SELECT A.* FROM (SELECT employee_id,
CASE 
    WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
    ELSE 0 END AS bonus
FROM employees ) A ORDER BY  A.employee_id