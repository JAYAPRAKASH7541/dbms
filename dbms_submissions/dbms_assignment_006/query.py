Q1='SELECT MOVIEWITHCAST.FNAME,MOVIEWITHCAST.LNAME FROM(ACTOR INNER JOIN CAST ON ID==PID) AS MOVIEWITHCAST WHERE MOVIEWITHCAST.MID==12148'
Q2='SELECT COUNT(MOVIEWITHCAST.ID) FROM (ACTOR INNER JOIN CAST ON ID==PID) AS MOVIEWITHCAST WHERE MOVIEWITHCAST.FNAME="Harrison (I)" AND MOVIEWITHCAST.LNAME="Ford"'
Q3='SELECT DISTINCT(MOVIEWITHCAST.PID) FROM(CAST INNER JOIN MOVIE ON MID==ID) AS MOVIEWITHCAST WHERE MOVIEWITHCAST.NAME LIKE "Young Latin Girls%"'
Q4='SELECT COUNT(DISTINCT(MOVIEWITHCAST.PID)) FROM (CAST INNER JOIN MOVIE ON MID==ID) AS MOVIEWITHCAST WHERE MOVIEWITHCAST.YEAR BETWEEN 1990 AND 2000'
