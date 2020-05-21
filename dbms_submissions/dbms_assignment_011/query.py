27|4|4
44|5|9
52|4|33
65|3|6
100|0|2
101|5|7
168|2|2
171|5|7
176|1|6
195|6|2
250|1|0
261|2|1
292|4|21
322|6|25
341|5|14
344|19|33
345|11|12
351|1|3
359|4|8
374|6|4
379|1|1
405|4|9
417|0|2
428|6|13
431|6|9
455|5|10
487|5|24
565|1|5
566|0|1
574|3|3
627|5|26
640|0|1
641|2|7
649|0|9
665|2|9
679|1|3
707|3|7
713|19|22
793|7|0
801|1|1
842|2|2
856|0|3
857|0|1
893|7|5
898|1|0
919|3|7
951|0|1
961|0|2
1019|4|11
1091|4|7
1099|8|20
1104|1|4
1121|6|22
1130|0|5
1140|9|55
1154|4|5
1231|5|5
1238|4|5
1246|5|1
1263|4|1
1287|1|0
1338|4|14
1339|1|3
1354|5|5
1356|3|6
1360|6|13
1400|18|15
1415|3|7
1425|5|7
1462|13|11
1473|10|9
1488|8|23
1519|3|11
1525|2|2
1542|1|2
1543|3|13
1547|0|2
1575|5|4
1578|19|27
1592|2|0
1601|3|2
1608|5|5
1622|0|1
1624|0|90
1630|1|2
1635|1|20
1638|4|7
1663|2|7
1673|16|27
1681|26|47
1715|3|5
1725|18|24
1731|2|1
1734|15|23
1787|19|36
1844|3|7
1868|13|63
1880|2|3
2045|0|3
2057|3|6
 
 
 
Q5='''
select distinct male_count.movie_id,female_count.no_of_female_actors,male_count.no_of_male_actors
from (select m.id as movie_id,
count(gender) as no_of_female_actors from actor
inner join cast on `cast`.pid=`actor`.id inner join 
movie m on `m`.id=`cast`.mid where gender="F" and `cast`.mid=`m`.id group by movie_id) as 
female_count join(select m1.id as movie_id,
count(gender) as no_of_male_actors from actor 
inner join cast on `cast`.pid=`actor`.id inner join 
movie m1 on `m1`.id=`cast`.mid where gender="M" and `cast`.mid=`m1`.id
group by movie_id) as 
male_count 
on `female_count`.movie_id==`male_count`.movie_id
limit 100
'''
 actor.id,actor.fname,actor.lname,actor.gender
 select  actor.id,actor.fname,actor.lname,actor.gender
from actor inner join cast on `cast`.pid=`actor`.id 
inner join movie on `cast`.mid=`movie`.id 
where name like "Annie%" and `actor`.id=`cast`.pid



 
