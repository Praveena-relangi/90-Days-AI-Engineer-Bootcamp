select count(*)
from SuperStore;

select sum(Sales)
from SuperStore;

select avg(Sales)
from SuperStore;

SELECT Category,
       SUM(Sales)
FROM SuperStore
GROUP BY Category;

SELECT Region,
       SUM(Sales)
FROM SuperStore
GROUP BY Region;

SELECT Segment, avg(Sales)
from SuperStore
group by Segment;

SELECT Category, SUM(Sales)
from SuperStore
group by Category
having sum(Sales) > 700000;

select Region, sum(Sales), avg(Sales), max(Sales), min(Sales)
from SuperStore
group by Region;