#https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/


select customer_number from (select count(customer_number) as order_count,customer_number from orders
group by customer_number
order by order_count desc) as TB1
limit 1;


