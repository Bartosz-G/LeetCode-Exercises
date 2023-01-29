#https://leetcode.com/problems/group-sold-products-by-the-date/


#Almost correct
SELECT sell_date,count(product) as num_sold, GROUP_CONCAT(product order by product) as products
FROM (select distinctrow sell_date,product from Activities) as Activities
GROUP BY sell_date
order by sell_date;

