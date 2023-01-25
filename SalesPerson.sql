#https://leetcode.com/problems/sales-person/

select name from SalesPerson
where sales_id not in (select Orders.sales_id from Company,Orders
where Orders.com_id = Company.com_id and Company.name = 'RED');