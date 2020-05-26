def write_data(sql_query):
	import sqlite3
	connection = sqlite3.connect("students.sqlite3")
	#connection = sqlite3.connect("dbms/dbms_resources/students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute("PRAGMA foreign_keys=on;") 
	crsr.execute(sql_query) 
	connection.commit() 
	connection.close()

def read_data(sql_query):
	import sqlite3 
	connection = sqlite3.connect("students.sqlite3")
	#connection = sqlite3.connect("dbms/dbms_resources/students.sqlite3")
	crsr = connection.cursor() 
	crsr.execute(sql_query) 
	ans= crsr.fetchall()
	connection.close() 
	return ans


class InvalidField(Exception):
	pass
class Student:
	#student_id=0
	mem='avg'
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
	def avg(cls,field,**key):
		'''if field not in ('name','age','student_id','score'):
			raise InvalidField'''
		cls.mem='avg'
		x=Student.filter(field,**key)
		return x[0][0]
	@classmethod
	def min(cls,field,**key):
		cls.mem='min'
		x=Student.filter(field,**key)
		return x[0][0]
	@classmethod
	def max(cls,field,**key):
		'''if field not in ('name','age','student_id','score'):
			raise InvalidField'''
		cls.mem='max'
		x=Student.filter(field,**key)
		return x[0][0]
	@classmethod
	def count(cls,field=None,**key):
		if field is None:
			query='select count(*) from student'
			x=read_data(query)
			return x[0][0]
		'''if field not in ('name','age','student_id','score'):
			raise InvalidField'''
		cls.mem='count'
		
		x=Student.filter(field,**key)
		return x[0][0]
	@classmethod
	def sum(cls,field=None,**key):

		cls.mem='sum'
		x=Student.filter(field,**key)
		return x[0][0]
	@classmethod
	def filter(cls,field=None,**key):
		cls.li=[]
		cls.le=[]
		cls.fields=field
		if field not in ('name','age','student_id','score'):
				raise InvalidField
		for k,v in key.items():
			field=k                                                                  
			b=v
			field=field.split("__")
			if field[0] not in ('name','age','student_id','score'):
				raise InvalidField
			if len(field)>1:
				if field[1]=='gt':
					query='{} > {}'.format(field[0],b)
				
				elif field[1]=='lt':
					query=' {} < {}'.format(field[0],b)
				
				elif field[1]=='lte':
					query=' {} <= {}'.format(field[0],b)
				
				elif field[1]=='gte':
					query=' {} >= {}'.format(field[0],b)
				
				elif field[1]=='neq':
	
					query=' {} <> {}'.format(field[0],b)
	
				elif field[1]=='contains':
					query=' {}  like "%{}%"'.format(field[0],b)
						
				elif field[1]=='in':
					query=' {} in {}'.format(field[0],tuple(b))
				
			elif len(field)==1:
				query=' {} ="{}"'.format(field[0],b)
			cls.le.append(query)
			x=' and '.join(cls.le)
		if len(key)>=1:
			x='select {}({}) from student where '.format(cls.mem,cls.fields)+x
			
		else:
			x='select {}({}) from student'.format(cls.mem,cls.fields)
		#print(x)
		ans=read_data(x)
		return ans

'''sum_of_age = Student.count("",age__lt=20)
print(sum_of_age)'''