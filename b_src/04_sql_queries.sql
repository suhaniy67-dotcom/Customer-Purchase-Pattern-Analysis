SELECT COUNT(*) AS Total_Rows
FROM cleaned_online_retail;
SELECT ROUND(SUM(Quantity * Price), 2) AS Total_Revenue
FROM cleaned_online_retail;
SELECT COUNT(DISTINCT Invoice) AS Total_Orders
FROM cleaned_online_retail;
SELECT COUNT(DISTINCT `Customer ID`) AS Total_Customers
FROM cleaned_online_retail;
SELECT Description,
       SUM(Quantity) AS Total_Quantity
FROM cleaned_online_retail
GROUP BY Description
ORDER BY Total_Quantity DESC
LIMIT 10;
SELECT `Customer ID`,
       ROUND(SUM(Quantity * Price), 2) AS Revenue
FROM cleaned_online_retail
GROUP BY `Customer ID`
ORDER BY Revenue DESC
LIMIT 10;
SELECT Country,
       ROUND(SUM(Quantity * Price), 2) AS Revenue
FROM cleaned_online_retail
GROUP BY Country
ORDER BY Revenue DESC;
SELECT ROUND(
    SUM(Quantity * Price) /
    COUNT(DISTINCT Invoice), 2
) AS Average_Order_Value
FROM cleaned_online_retail;
SELECT strftime('%Y-%m', InvoiceDate) AS Month,
       ROUND(SUM(Quantity * Price), 2) AS Revenue
FROM cleaned_online_retail
GROUP BY Month
ORDER BY Month;
SELECT strftime('%Y-%m', InvoiceDate) AS Month,
       COUNT(DISTINCT Invoice) AS Orders
FROM cleaned_online_retail
GROUP BY Month
ORDER BY Month;
SELECT Description,
       ROUND(SUM(Quantity * Price), 2) AS Revenue
FROM cleaned_online_retail
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 10;
SELECT Country,
       COUNT(DISTINCT Invoice) AS Orders
FROM cleaned_online_retail
GROUP BY Country
ORDER BY Orders DESC
LIMIT 10;
SELECT ROUND(AVG(Quantity), 2) AS Average_Quantity
FROM cleaned_online_retail;
SELECT Invoice,
       ROUND(SUM(Quantity * Price), 2) AS Order_Value
FROM cleaned_online_retail
GROUP BY Invoice
ORDER BY Order_Value DESC
LIMIT 1;
