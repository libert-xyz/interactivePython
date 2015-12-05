class Person(object):

	def __init__(self,fn,ln,a):
		self.first_name = fn
		self.last_name = ln
		self.age = a

	def __str__(self):

		return self.first_name + " , " + self.last_name



class Student(Person):

	def __init__(self,fn,ln,a,g):
		super(Student,self).__init__(fn,ln,a)
		self.grades = g


	def __str__(self):
		return self.first_name + " " + self.last_name + ": " +" Average Grades: " + str(self.getAverage())

	def getAverage(self):

		s = 0
		for i in self.grades:
			s = s + i
		
		return s/len(self.grades)


