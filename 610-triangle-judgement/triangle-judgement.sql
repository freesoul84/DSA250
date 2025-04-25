
/*SELECT x,y,z, 
        CASE 
            WHEN (x + y >z) AND (x + z > y) AND (z + y > x) THEN 'Yes'
            ELSE 'No'
        END AS triangle
FROM Triangle*/

SELECT x,y,z,IF((x + y >z) AND (x + z > y) AND (z + y > x) ,'Yes','No') AS triangle FROM Triangle
