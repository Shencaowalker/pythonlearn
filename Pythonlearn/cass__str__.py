class student(object):
	__slots__=("name","age","score")
	def __init__(self,name):
		self.name=name
	def __str__(self):
		return "student object (name:%s)" %self.name
	def __len__(self):
		return "this is __len__."
	__repr__=__str__

