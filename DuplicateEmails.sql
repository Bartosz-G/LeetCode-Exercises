#https://leetcode.com/problems/duplicate-emails/submissions/881824494/

SELECT DISTINCT Person.email FROM (
    SELECT count(id),email FROM Person
        GROUP BY email
        HAVING count(id)>1)
    AS TB1,Person
    WHERE TB1.email = Person.email;