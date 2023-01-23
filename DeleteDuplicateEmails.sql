#https://leetcode.com/problems/delete-duplicate-emails/

#Works
delete from Person where Id in (select id from (Select Person.Id,TB1.rn from Person,
(SELECT Id,
     row_number() OVER(PARTITION BY Email ORDER BY Id) AS rn
  FROM Person) as TB1
where Person.Id = TB1.Id
having TB1.rn >1)as TB2);


