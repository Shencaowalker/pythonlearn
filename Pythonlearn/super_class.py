#!/usr/bin/python
class Animal(object):
 	def run(self):
		print "Animal is running..."

class  Dog(Animal):
	pass
class Cat(Animal):
	pass
class Dog1(Animal):
	def run(self):
		print('Dog is running...')
	def eat(self):
		print('Eating meat...')



if __name__=="__main__":
	dog=Dog()
	dog.run()
	cat=Cat()
	cat.run()
	dog1=Dog1()
	dog1.run()


