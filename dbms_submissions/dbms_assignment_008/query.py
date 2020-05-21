#Q1='SELECT ID,FNAME FROM DIRECTOR D WHERE EXISTS (SELECT COUNT(D.ID) FROM DIRECTOR GROUP BY YEAR HAVING COUNT(D.ID)>=1 AND YEAR>=2000)'

#Q1='select director.id,director.fname from director inner join moviedirector on `director`.id=`moviedirector`.did inner join movie on `movie`.id=`moviedirector`.mid where exists (select id,fname  from director where (select count(id) as m from movie where year>=2000)>=1)and  exists (select id,fname from director where (select count(id) as m from movie where year<2000)=0)'
Q3='select * from actor where id not in(select `actor`.id from actor inner join cast on `actor`.id==`cast`.pid inner join movie on `cast`.mid=`movie`.id where year between 1990 and 2000) order by `actor`.id desc limit 100'



Q1='SELECT D.ID,D.FNAME FROM DIRECTOR D WHERE EXISTS (SELECT M.ID FROM MOVIE M INNER JOIN MovieDirector MD ON M.ID=MD.MID WHERE MD.DID=D.ID AND YEAR>2000) AND NOT EXISTS (SELECT M.ID FROM MOVIE M INNER JOIN MovieDirector MD ON M.ID==MD.MID WHERE MD.DID=D.ID AND YEAR<2000) ORDER BY D.ID'
Q2='''select fname,
(SELECT NAME FROM MOVIE AS M INNER JOIN 
MOVIEDIRECTOR MD ON M.ID==MD.MID where 
MD.DID=d.id ORDER BY RANK DESC,NAME ASC LIMIT 1) 
from director d limit 100'''
Q3='''SELECT `ACTOR`.ID,`ACTOR`.FNAME,`ACTOR`.LNAME,`ACTOR`.GENDER FROM ACTOR
 WHERE NOT EXISTS (SELECT `ACTOR`.ID FROM ACTOR INNER JOIN CAST ON 
`ACTOR`.ID=`CAST`.PID INNER JOIN MOVIE ON 
`CAST`.MID=`MOVIE`.ID WHERE `MOVIE`.ID==`CAST`.MID AND 
YEAR BETWEEN 1990 AND 2000)''' 