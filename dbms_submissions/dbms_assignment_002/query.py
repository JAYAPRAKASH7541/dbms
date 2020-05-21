Q1='SELECT * FROM MOVIE ORDER BY RANK DESC LIMIT 10'
Q2='SELECT * FROM MOVIE ORDER BY RANK DESC LIMIT 10 OFFSET 10'
Q3='SELECT name FROM MOVIE WHERE YEAR>2004'
Q4='SELECT name FROM MOVIE WHERE RANK<1.1'
Q5='SELECT * FROM MOVIE WHERE YEAR IN(2004,2005,2006)'
Q6='SELECT name,year FROM MOVIE WHERE name LIKE "Harry%"'
Q7='SELECT * FROM ACTOR WHERE fname="Christin" AND lname!="Watson"'
#Christin 
Q8='SELECT * FROM ACTOR WHERE fname="Woody" AND lname="Watson"'
Q9='SELECT name FROM MOVIE WHERE YEAR=1990 AND RANK=5'
Q10='SELECT * FROM ACTOR WHERE fname="Christin" AND lname="Watson"'
Q11='SELECT NAME FROM MOVIE WHERE YEAR BETWEEN 2003 AND 2005'
Q12='SELECT DISTINCT YEAR FROM MOVIE'
#Q13='SELECT * FROM ACTOR WHERE (fname="Christin" OR lname="Watson") AND (GENDER="M") ORDER BY fname Limit 10'
Q13 = 'SELECT * FROM ACTOR WHERE (fname="Christin" OR lname="Watson") ORDER BY GENDER DESC LIMIT 10'        
                                                                                                  
                                                                                                