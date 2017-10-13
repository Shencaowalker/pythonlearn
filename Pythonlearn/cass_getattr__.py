#coding:utf-8
class student(object):
	def __init__(self):
		self.name="Michael"
	def __getattr__(self,attr):
		if attr=="score":
			return 99


class chain(object):
	def __init__(self,path=''):
		self._path=path
	def __getattr__(self,attr):
		return chain("%s/%s" % (self._path,attr))
	def __str__(self):
		return self._path
	__repr__=__str__


class callself(object):
	def __init__(self,name):
		self.name=name
	def __call__(self,call="shuai"):
		print "My name is %s. and the attr is %s" % (self.name,call)

class Hello(object):
	def hello(self,name='world'):
		print ("hello,%s." % name)
#创建一个class对象，type()函数依次传入３个参数：
#１class的名称
#２继承的父集合，注意python支持多重继承，多个（object,）
#３class的方法名称和函数绑定，这里是把fn绑定到hello上
#>>>Fn=type("Hello",(object,),dict(hello=fn))
class ListMetaclass(type):
	def __new__(cls,name,bases,attrs):
		attrs["add"]=lambda self,value:self.append(value)
		return type.__new__(cls, name, bases, attrs)
