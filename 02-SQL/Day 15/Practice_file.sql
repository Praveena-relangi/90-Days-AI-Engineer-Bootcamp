SELECT *
FROM SuperStore
LIMIT 5;

SELECT Category,
       Sales
FROM SuperStore
LIMIT 10;

SELECT *
FROM SuperStore
WHERE Category = 'Technology';

SELECT *
FROM SuperStore
WHERE Sales > 1000;

SELECT *
FROM SuperStore
ORDER BY Sales DESC
LIMIT 10;