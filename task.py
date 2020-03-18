class Tinkers:
	def __init__(self,name):
		self.stack=[]
		self.title=""
		self.name=name
		self.start=None
		self.end=None

	def addStacks(self,interest):
		self.stack.append(interest)

	def setMentorOrLearner(self,title):
		self.title=title

	def setAvailableTime(self,starttime,endtime):
	#This method sets time in hour in UTC
		if self.title=="Mentor":
			self.start=starttime
			self.end=endtime

	def getMentor(self,stack,time):
		if stack in self.stack and self.title=="Mentor":
			if time>=self.start and time<=self.end:
				return True
if __name__=="__main__":
	tinks=[]

	obj1=Tinkers("Praneet")
	obj1.addStacks("Java")
	obj1.setMentorOrLearner("Learner")
	tinks.append(obj1)
	
	obj4=Tinkers("Suresh")
	obj4.addStacks("Java")
	obj4.setMentorOrLearner("Learner")
	tinks.append(obj4)

	obj2=Tinkers("Sumit")
	obj2.addStacks("Java")
	obj2.setMentorOrLearner("Mentor")
	start=12
	end=17
	obj2.setAvailableTime(start,end)
	tinks.append(obj2)

	obj3=Tinkers("Ram")
	obj3.addStacks("Java")
	obj3.setMentorOrLearner("Mentor")
	start=5
	end=20
	obj3.setAvailableTime(start,end)
	tinks.append(obj3)

	stack="Java"
	time=14
	for obj in tinks:
		if obj.getMentor(stack,time):
			print(obj.name)
		