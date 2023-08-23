## Домашнее задание к Модулю 2
--

1. Установить PostgeSQL и DBeaver - **done**
2. Загрузить в базу таблицы orders, returns, people - **done** (использовала скрипты-заготовки [отсюда](https://github.com/Data-Learn/data-engineering/tree/master/DE-101%20Modules/Module02/DE%20-%20101%20Lab%202.1))
3.  Написать запросы для основных метрик:
	
  <br>- Total sales
  <br>- Total profit
  <br>- Profit Ratio = Gross profit / Net sales * 100%
```sql
select ROUND(sum(sales), 2) as total_sales, 
	ROUND(sum(profit), 2) as total_profit,
	ROUND(100 * sum(profit) / sum(sales), 2) as profit_ratio
from orders;
```
  <br>- Profit per Order
```sql
select order_id, ROUND(sum(profit), 2) as profit_per_order
from orders o 
group by order_id 
order by profit_per_order desc;
```
  <br>- Sales per Customer
```sql
select customer_name, ROUND(sum(sales), 2) as sales_per_customer
from orders o 
group by customer_name
order by sales_per_customer DESC;
```
  <br>- Avg. Discount
```sql
select round(avg(discount), 2) as avg_discount
from orders o;
```
  <br>- Monthly Sales by Segment
```sql
select segment, date_part('month', order_date) as month, sum(sales) as sales_sum
from orders o 
group by segment, date_part('month', order_date)
order by segment, month;
```
  <br>- Monthly Sales by Product Category
```sql
select category, date_part('month', order_date) as month, sum(sales) as sales_sum
from orders o 
group by category, date_part('month', order_date)
order by category, month;
```
<br> - Sum Sales of returned orders
```sql
select sum(sales)
from orders o 
inner join (select distinct order_id from "returns" r) dr 
on dr.order_id = o.order_id;
```


скрипт [выложить на github](https://github.com/KateKryukova/Learning_Path/blob/main/DataLearn/DE-101/Module_2/Key_metrics_overview.sql) - **done** 

   ![alt text](https://github.com/KateKryukova/Learning_Path/blob/main/DataLearn/DE-101/Module_2/results-2.PNG?raw=true)
