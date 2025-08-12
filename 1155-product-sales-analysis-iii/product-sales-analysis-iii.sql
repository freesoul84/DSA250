# Write your MySQL query statement below
SELECT A.product_id, A.year as first_year, A.quantity, A.price
FROM Sales A
WHERE (A.product_id,A.year) IN 
(SELECT product_id, MIN(year)
FROM Sales GROUP BY product_id)