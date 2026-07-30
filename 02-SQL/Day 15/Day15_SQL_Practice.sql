-- Display all records
SELECT *
FROM SuperStore;

-- Display Customer Name and Sales
SELECT "Customer Name", Sales
FROM SuperStore;

-- Display orders where Sales > 1000
SELECT *
FROM SuperStore
WHERE Sales > 1000;

-- Sort by Sales
SELECT *
FROM SuperStore
ORDER BY Sales DESC;

-- Top 10 highest sales
SELECT *
FROM SuperStore
ORDER BY Sales DESC
LIMIT 10;