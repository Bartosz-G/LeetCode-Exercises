#https://leetcode.com/problems/employees-earning-more-than-their-managers/

select name AS Employee FROM
(SELECT t1.name, t1.salary as s1,t2.salary as s2 FROM employee t1, employee t2
WHERE t1.managerId = t2.id
HAVING t1.salary > t2.salary) AS DT1;


