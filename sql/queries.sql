SELECT *
FROM employees;

SELECT *
FROM orders;

SELECT Department,
       AVG(Salary) AS Average_Salary
FROM employees
GROUP BY Department;
