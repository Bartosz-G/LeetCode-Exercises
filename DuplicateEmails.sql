#https://leetcode.com/problems/duplicate-emails/submissions/881824494/

SELECT email FROM Person GROUP BY email HAVING COUNT(email)>1;