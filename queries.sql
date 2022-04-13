SELECT * FROM Customers
where city="Berlin"


SELECT * FROM Customers
where city="México D.F."


SELECT AVG(price) as Average_Price FROM Products


SELECT count(price) from products
where price=18


SELECT * FROM Orders
where OrderDate between "1996-08-01" and "1996-09-06"


select CustomerID, Count(*) customer_count from orders
group by CustomerID
having customer_count>3


SELECT c1.CustomerName, c1.city
from Customers c1
where c1.city IN (SELECT city FROM Customers GROUP BY CITY HAVING COUNT(*) > 1)


