#!/usr/bin/python
#coding:utf-8
import functools
import time
def log(func):
	def wrapper(*args,**kw):
		print "call %s():" % func.__name__
		return func(*args,**kw)
	return wrapper




def log1(text):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print "%s  %s()" %(text,func.__name__)
			return func(*args,**kw)
		return wrapper
	return decorator




def log2(first):
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args,**kw):
			print "%s   %s():" %(first,func.__name__)
			func(*args,**kw)
		return wrapper
	if isinstance(first,str):
		return decorator
	else:
		def decorator2(*args,**kw):
			print "Null  %s():" % first.__name__
			first(*args,**kw)
		return decorator2

if __name__=="__main__":
	@log1("execute")
	def now1():
		print time.time()
	
	now1()
	print now1.__name__


	@log
	def now():
		print  time.time()

	now()
	print now.__name__
	#上面的例子相当与now=log(now)  即now()=log(now)()
	@log2("hahaha")
	def now2():
		print time.time()
	now2()

	@log2
	def now2():
		print time.time()

	now2()

