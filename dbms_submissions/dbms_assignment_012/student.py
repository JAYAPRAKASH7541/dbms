'''def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3 
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
class DoesNotExist(Exception):
	pass
class MultipleObjectsReturned(Exception):
	pass
class InvalidField(Exception):
	pass
class Student:
	student_id=0
	a=''
	b=0
	def __init__(self,name,age, score):
	    self.name = name
	    self.age = age
	    self.student_id=None
	    self.score = score
	    
	  
	    	
	@classmethod
	def get(cls,**key):
		import sqlite3
		connection = sqlite3.connect("students.sqlite3")
		crsr = connection.cursor()
		for k,v in key.items():
			cls.a=k
			cls.b=v
		if cls.a!='student_id' and cls.a!='name' and cls.a!='age' and cls.a!='score':
			raise InvalidField("InvalidField:")
		sql_query="select * from student where {}={}".format(cls.a,cls.b)
		crsr.execute(sql_query)
		ans= crsr.fetchall()
		connection.close()
		
		if len(ans)==0:
			raise DoesNotExist("DoesNotExist:")
		if len(ans)>1:
			raise MultipleObjectsReturned("MultipleObjectsReturned:")
		else:
			ans=tuple(ans[0])
			#cls.student_id=cls.b
			obj=Student(ans[1],ans[2],ans[3])
			obj.student_id=ans[0]
			return obj
	@classmethod
	def delete(cls):
		import sqlite3
		connection = sqlite3.connect("students.sqlite3")
		crsr = connection.cursor()
		sql_query="delete from student where {}={}".format(cls.a,cls.b)
		crsr.execute(sql_query)
		connection.commit()
		connection.close()
	def save(self):
		import sqlite3
		connection = sqlite3.connect("dbms/dbms_resources/students.sqlite3")
		crsr = connection.cursor()
		if self.student_id is None:
			query="insert into student(name,age,score)values('{}',{},{})".format(self.name,self.age,self.score)
			crsr.execute(query)
			connection.commit()
			q1='select student_id from student where name="{}" and age={} and score={}'.format(self.name,self.age,self.score)
			crsr.execute(q1)
			r1= crsr.fetchall()
			self.student_id=r1[0][0] 
			connection.commit()
			connection.close()
		else:
			query1="update student set name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.b)
			crsr.execute(query1)
			connection.commit()
			connection.close()'''
def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3 
	connection = sqlite3.connect("students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()  
	connection.close() 
	return ans
class DoesNotExist(Exception):
	pass
class MultipleObjectsReturned(Exception):
	pass
class InvalidField(Exception):
	pass
class Student:
	#student_id=0
	
	def __init__(self,name,age, score):
	    self.name = name
	    self.age = age
	    self.student_id=None
	    self.score = score
	    

	@classmethod
	def get(cls,**key):
		for k,v in key.items():
			cls.a=k
			cls.b=v
		if cls.a!='student_id' and cls.a!='name' and cls.a!='age' and cls.a!='score':
			raise InvalidField
		
		sql_query="select * from student where {}='{}'".format(cls.a,cls.b)
		ans=read_data(sql_query)
		if len(ans)==0:
			raise DoesNotExist
		if len(ans)>1:
			raise MultipleObjectsReturned
		
		ans=tuple(ans[0])
		obj=Student(ans[1],ans[2],ans[3])
		obj.student_id=ans[0]
		return obj
	@classmethod
	def delete(cls):
		sql_query="delete from student where {}={}".format(cls.a,cls.b)
		write_data(sql_query)

	def save(self):
		if self.student_id is None:
			query="insert into student(name,age,score)values('{}',{},{})".format(self.name,self.age,self.score)
			write_data(query)
			q1='select student_id from student where name="{}" and age={} and score={}'.format(self.name,self.age,self.score)
			r1=read_data(q1)
			self.student_id=r1[0][0] 
			
		else:
			query1="update student set name='{}',age={},score={} where student_id={}".format(self.name,self.age,self.score,self.b)
			write_data(query1)
	


