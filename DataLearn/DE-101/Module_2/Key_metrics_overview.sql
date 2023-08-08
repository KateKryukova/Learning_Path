--Total Sales
--Total Profit
--Profit Ratio = Gross profit / Net sales * 100
select ROUND(sum(sales), 2) as total_sales, 
	ROUND(sum(profit), 2) as total_profit,
	ROUND(100 * sum(profit) / sum(sales), 2) as profit_ratio
from orders;


--Profit per Order
select order_id, ROUND(sum(profit), 2) as profit_per_order
from orders o 
group by order_id 
order by profit_per_order desc;

--Sales per Customer
select customer_name, ROUND(sum(sales), 2) as sales_per_customer
from orders o 
group by customer_name
order by sales_per_customer DESC;

--Avg. Discount
select round(avg(discount), 2) as avg_discount
from orders o;

--Monthly Sales by Segment
select segment, date_part('month', order_date) as month, sum(sales) as sales_sum
from orders o 
group by segment, date_part('month', order_date)
order by segment, month;

--Monthly Sales by Product Category
select category, date_part('month', order_date) as month, sum(sales) as sales_sum
from orders o 
group by category, date_part('month', order_date)
order by category, month;
