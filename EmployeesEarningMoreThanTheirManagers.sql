#https://leetcode.com/problems/employees-earning-more-than-their-managers/

select name as Employee from
(select t1.name, t1.salary as s1,t2.salary as s2 from employee t1, employee t2
where t1.managerId = t2.id
having t1.salary > t2.salary) as DT1;


