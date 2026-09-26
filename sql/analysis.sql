SELECT Product,
       SUM(Amount) AS Total_Sales
FROM orders
GROUP BY Product
ORDER BY Total_Sales DESC;
