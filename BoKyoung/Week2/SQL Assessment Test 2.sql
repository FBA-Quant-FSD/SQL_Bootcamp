## SQL Assessment Test 2

# 1
SELECT * FROM cd.facilities

#2
SELECT name,membercost FROM cd.facilities

#3
SELECT * 
FROM cd.facilities
WHERE membercost >0;

#4
SELECT facid,name,membercost,monthlymaintenance 
FROM cd.facilities
WHERE membercost >0
AND membercost < 0.02*monthlymaintenance

#5
SELECT * FROM cd.facilities
WHERE name LIKE '%Tennis%'

#6
SELECT *
FROM cd.facilities
WHERE facid IN (1,5)

##7 - 날짜 사용
SELECT memid,surname,firstname,joindate
from cd.members
WHERE joindate >= '2012-09-1'
#(>= 대신 >를 써도 동일한 결과가 나옴 - 9월 1일이 포함됨)

#8
SELECT DISTINCT surname 
FROM cd.members
ORDER BY surname
LIMIT 10

#9
SELECT surname,firstname,joindate 
from cd.members
ORDER BY joindate DESC
LIMIT 1;

#10
SELECT DISTINCT COUNT(*)
FROM cd.facilities
WHERE guestcost >= 10

#11
SELECT facid,SUM(slots)
AS num_slots
FROM cd.bookings
WHERE starttime >= '2012-09-01'
and starttime <'2012-10-01'
GROUP BY facid
ORDER BY num_slots

#(WHERE BETWEEN '2012-09-1' AND '2012-09-30')과 결과가 다르게 나온다

SELECT facid,SUM(slots)
AS num_slots
FROM cd.bookings
WHERE starttime BETWEEN '2012-09-01'
AND '2012-10-01'
GROUP BY facid
ORDER BY num_slots

# 이렇게 해야 같게 나온다


#12
SELECT facid,SUM(slots)
AS total_slots
FROM cd.bookings
GROUP BY facid
HAVING SUM(slots) >1000
ORDER BY facid

#13
#(오류) - 2012.09.21 자료 찾기
SELECT starttime AS start, name
FROM cd.bookings
INNER JOIN cd.facilities
ON cd.bookings.facid = cd.facilities.facid
WHERE cd.facilities.facid IN (0,1)
AND starttime >= '2012-09-21'
AND starttime <= '2012-09-21' # 이렇게 하면 안 나옴
ORDER BY starttime

#(맞은것1)
SELECT starttime AS start, name
FROM cd.bookings
INNER JOIN cd.facilities
ON cd.bookings.facid = cd.facilities.facid
WHERE cd.facilities.facid IN (0,1)
AND starttime >= '2012-09-21'
AND starttime < '2012-09-22' # 이렇게 해야 나옴
ORDER BY starttime

#(맞은것2)
SELECT starttime AS start, name
FROM cd.bookings
INNER JOIN cd.facilities
ON cd.bookings.facid = cd.facilities.facid
WHERE cd.facilities.facid IN (0,1)
AND starttime
BETWEEN '2012-09-21' AND '2012-09-22' # 이렇게 해도 된다!
ORDER BY starttime


#14
SELECT starttime
FROM cd.bookings
INNER JOIN cd.members
ON cd.bookings.memid = cd.members.memid
WHERE surname = 'Farrell' AND firstname = 'David'