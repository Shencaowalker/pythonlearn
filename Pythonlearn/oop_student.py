#!/usr/bin/bash
#coding:utf-8
std1={"name":"shencao","score":98}
std2={"name":"shenyan","score":81}

def print_score(std):
	print "this student and name is %s and he score is %s!" %(std["name"],std["score"])

print_score(std1)
print_score(std2)

class student(object):
	def __init__(self,name,score,sex):
		self.name=name
		self.score=score
		self.__sex=sex
	def print_score(self):
		print "this student sex is %s and  name is %s and he score is %s!" %(self.__sex,self.name,self.score)
	def get_grade(self):
		if self.score >=90:
			return "A"
		elif self.score >=60:
			return "B"
		else:
			return "C"
	def get_sex(self):
		return self.__sex
if __name__=="__main__":

	shencao1=student("shencao",100,"nan")
	shencao1.print_score()
	print shencao1.get_grade()
	print shencao1.get_sex()
	print shencao1._student__sex()
#上面的一句是说把__sex转换成_student__sex这样了


