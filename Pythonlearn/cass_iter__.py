class fib(object):
	def __init__(self):	
		self.a,self.b=0,1
	def __iter__(self):
		return self
	def __next__(self):
		self.a,self.b=self.b,self.a+self.b
		if self.a >100000:
			raise StopIteration()
		return self.a

class fib2(object):
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b=1,1
			for i in range(n):
				a,b=b,a+b
			return a
		if isinstance(n,slice):
			start=n.start
			stop=n.stop
			if start is None:
				start=0
			a,b=1,1
			l=[]
			for i in range(stop):
				l.append(a)
				a,b=b,a+b

			return l

			

if __name__=="__main__":
	f=fib2()
	print f[2]
	print f[3:6]


