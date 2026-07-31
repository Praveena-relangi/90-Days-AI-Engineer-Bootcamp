SELECT Customers.Customer_Name, Orders.Order_ID
FROM Customers
INNER JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID

SELECT Customers.Customer_Name, Orders.Product
FROM Customers
LEFT JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID

SELECT Customers.Customer_Name, SUM(Orders.Sales) AS TOTAL_SALES 
FROM Customers 
LEFT JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID 
GROUP BY Customer_Name

SELECT c.Customer_ID, c.Customer_Name
FROM Customers c
LEFT JOIN Orders o
    ON c.Customer_ID = o.Customer_ID
WHERE o.Customer_ID IS NULL;

SELECT c.Customer_ID, c.Customer_Name, COUNT(o.Order_ID) AS OrderCount
FROM Customers c
JOIN Orders o
    ON c.Customer_ID = o.Customer_ID
GROUP BY c.Customer_ID, c.Customer_Name
HAVING COUNT(o.Order_ID) > 1;