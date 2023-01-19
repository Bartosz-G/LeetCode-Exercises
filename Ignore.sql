#Despite the name you haven't ignored this file... nothing to see here, just some queries I'd like to remember




#Queries for EmployeesEarnings
#Correctly chooses employees with a manager
SELECT * from employee
    where managerId in (select id from employee);

#Correctly chooses managers with employee
select * from employee
    where id in (select managerId from employee);


#Correctly merges based on managerId
select * from employee t1, employee t2
where t1.managerId = t2.id;


#Correctly joined table
select * from employee t1, employee t2
where t1.managerId = t2.id
having t1.salary > t2.salary;


#Final solution
select name from
(select t1.name, t1.salary as s1,t2.salary as s2 from employee t1, employee t2
where t1.managerId = t2.id
having t1.salary > t2.salary) as DT1;