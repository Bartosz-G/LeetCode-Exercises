#https://leetcode.com/problems/combine-two-tables/description/

SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Person
LEFT JOIN Address ON Person.personId=Address.personId
UNION
SELECT Person.firstName, Person.lastName, Address.city, Address.state
FROM Address
RIGHT JOIN Person ON Person.personId=Address.personId;