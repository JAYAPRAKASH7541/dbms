def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("selected_students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3 
	connection = sqlite3.connect("selected_students.sqlite3")
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
	    
	def __repr__(self):
		return "Student(student_id={}, name={}, age={}, score={})".format(
        self.student_id,
        self.name,
        self.age,
        self.score)
	@classmethod
	def get(cls,**key):
		for k,v in key.items():
			cls.a=k
			cls.b=v
		if cls.a!='student_id' and cls.a!='name' and cls.a!='age' and cls.a!='score':
			raise InvalidField
		if cls.a=='name':
			sql_query="select * from student where {}='{}'".format(cls.a,cls.b)
		else:
			sql_query="select * from student where {}={}".format(cls.a,cls.b)
		
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
			query1="update student set student_id={},name='{}',age={},score={} where student_id={}".format(self.student_id,self.name,self.age,self.score,self.b)
			write_data(query1)
	@classmethod
	def filter(cls,**key):
		cls.li=[]
		cls.le=[]
		cls.attr='select * from student where'
		for k,v in key.items():
			cls.f=k                                                                  
			cls.op=v
			field=cls.f
			field=field.split("__")
			if field[0] not in ('name','age','student_id','score'):
				raise InvalidField
			if len(field)>1:
				#print("mouni")
				if field[1]=='gt':
					query='{}>"{}"'.format(field[0],cls.op)
				
				elif field[1]=='lt':
					query='{}<"{}"'.format(field[0],cls.op)
					
				elif field[1]=='gte':
					query='{}>="{}"'.format(field[0],cls.op)
					
				elif field[1]=='neq':

					query='{}<>"{}"'.format(field[0],cls.op)
	
				elif field[1]=='gte':
					query='{}>="{}"'.format(field[0],cls.op)

				elif field[1]=='lte':
					query='{}<="{}"'.format(field[0],cls.op)
	
				elif field[1]=='contains':
					query='{} like "%{}%"'.format(field[0],cls.op)
					
				elif field[1]=='in':
					query='{} in {}'.format(field[0],tuple(cls.op))
					
			elif len(field)==1:
				query='{}="{}"'.format(cls.f,cls.op)
			cls.le.append(query)
			x=' and '.join(cls.le)
		x='select * from student where '+x
		
		ans=read_data(x)
		
		for i in range (len(ans)):
			obj=Student(ans[i][1],ans[i][2],ans[i][3])
			obj.student_id=ans[i][0]
			cls.li.append(obj)
		return cls.li
