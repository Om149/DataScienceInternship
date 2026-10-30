SELECT DATE_FORMAT(OrderDate, '%Y-%m') AS Month,
       SUM(Quantity * UnitPrice) AS TotalRevenue
FROM Sales
GROUP BY DATE_FORMAT(OrderDate, '%Y-%m')
ORDER BY Month;
 
-- SQL 2: Revenue by Category
SELECT Category,
       SUM(Quantity * UnitPrice) AS TotalRevenue
FROM Sales
GROUP BY Category
ORDER BY TotalRevenue DESC;
 
-- SQL 3: Revenue by Region
SELECT Region,
       SUM(Quantity * UnitPrice) AS TotalRevenue,
       COUNT(*) AS OrderLines
FROM Sales
GROUP BY Region
ORDER BY TotalRevenue DESC;
 
-- SQL 4: Customer Revenue
SELECT CustomerID,
       SUM(Quantity * UnitPrice) AS TotalRevenue,
       COUNT(*) AS OrderLines
FROM Sales
GROUP BY CustomerID
ORDER BY TotalRevenue DESC;
 
-- SQL 5: Product Quantity and Revenue
SELECT Product,
       SUM(Quantity) AS UnitsSold,
       SUM(Quantity * UnitPrice) AS TotalRevenue
FROM Sales
GROUP BY Product
ORDER BY UnitsSold DESC;
