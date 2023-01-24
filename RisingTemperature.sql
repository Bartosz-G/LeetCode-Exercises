#https://leetcode.com/problems/rising-temperature/


select TB1.id from Weather as TB1,Weather as TB2
where subdate(TB1.recordDate,1) = TB2.recordDate and TB1.temperature > TB2.temperature;