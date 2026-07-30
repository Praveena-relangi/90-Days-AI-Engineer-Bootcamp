select Segment, count(*) 
from SuperStore
group by Segment;

select State, sum(Sales)
from SuperStore
group by State;

select Category, avg(Sales)
from SuperStore
group by Category;

select Region, sum(Sales) 
from SuperStore
group by Region
having sum(Sales) > 500000;

select Category, sum(Sales), max(Sales)
from SuperStore 
group by Category;