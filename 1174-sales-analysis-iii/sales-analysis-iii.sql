/* Write your T-SQL query statement below */
SELECT DISTINCT A.product_id, A.product_name
FROM Product A 
INNER JOIN Sales B
ON A.product_id = B.product_id
WHERE B.sale_date BETWEEN '2019-01-01' and '2019-03-31'
and A.product_id NOT IN (SELECT C.product_id
FROM Product C
INNER JOIN Sales D
ON C.product_id = D.product_id
WHERE D.sale_date NOT BETWEEN '2019-01-01' and '2019-03-31')