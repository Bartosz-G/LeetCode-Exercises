#https://leetcode.com/problems/combine-two-tables/description/

SELECT P.firstName, P.lastName, A.city, A.state
FROM Person P
LEFT JOIN Address A USING (personId)