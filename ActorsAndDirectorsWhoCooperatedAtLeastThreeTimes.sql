#https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/


SELECT TB2.actor_id,TB2.director_id
FROM (SELECT TB1.actor_id, TB1.director_id, COUNT(*) as duplicate_count
FROM (select actor_id,director_id from ActorDirector) as TB1
GROUP BY TB1.actor_id, TB1.director_id
HAVING COUNT(*) > 1) AS TB2
WHERE TB2.duplicate_count >= 3;