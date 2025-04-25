# Write your MySQL query statement below
SELECT name,population,area
FROM World
WHERE area >= (3*1000000) OR population >= (25*1000000)