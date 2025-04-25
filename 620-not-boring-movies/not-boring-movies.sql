# Write your MySQL query statement below

SELECT id,movie, description,rating
FROM Cinema
WHERE id % 2 = 1 AND LOWER(TRIM(description)) NOT LIKE '%boring%'
ORDER BY rating DESC