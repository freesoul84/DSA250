SELECT user_id,email
FROM Users
WHERE email LIKE '[a-zA-Z0-9_]%@[a-zA-Z]%.com' AND
    email NOT LIKE '%..%' AND 
    email NOT LIKE '%.%@%' AND
    email NOT LIKE '%@[a-zA-Z]%[0-9]%'
ORDER BY user_id