CREATE TABLE Customers (Customer_ID INTEGER PRIMARY KEY, 
Customer_Name TEXT
);

INSERT INTO Customers VALUES
(101, 'Praveena'),
(102, 'Niranjan'),
(103, 'Rudransh'),
(104, 'Vikas')

SELECT * FROM Customers;

CREATE TABLE Orders (
   Order_ID INTEGER PRIMARY KEY,
   Customer_ID INTEGER,
   Product TEXT,
   Sales REAL
 );
 
 INSERT INTO Orders VALUES
(1,101,'Laptop',80000),
(2,101,'Mouse',1000),
(3,103,'Keyboard',2000),
(4,105,'Monitor',15000);

SELECT * FROM Orders;

SELECT
Customers.Customer_Name,
Orders.Product,
Orders.Sales
FROM Customers
INNER JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID;

SELECT
Customers.Customer_Name,
Orders.Product,
Orders.Sales
FROM Customers
LEFT JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID;

SELECT
Customers.Customer_Name,
COUNT(Orders.Order_ID) AS Total_Orders
FROM Customers
LEFT JOIN Orders
ON Customers.Customer_ID = Orders.Customer_ID
GROUP BY Customers.Customer_Name;

