#!/usr/bin/python


def jianfunc(s):
	s_jian_list=s.split("-")
	if len(s_jian_list)>1:
		b=cengfunc(s_jian_list[0])
		for i in s_jian_list[1:]:
			b=b-cengfunc(i)
		return b
	else:
		return cengfunc(s_jian_list[0])
def cengfunc(s):
	c=1
	s_ceng_list=s.split("*")
	for i in s_ceng_list:
		c=c*chufunc(i)
	return c

def chufunc(s):
	s_chu_list=s.split("/")
	if len(s_chu_list)>1:
		d=chufunc(s_chu_list[0])
		for i in s_chu_list[1:]:
			d=d/chufunc(i)
		return d
	else:
		return int(s_chu_list[0])




posture=''
while posture !="end":
	try:
		posture=raw_input("Please enter the shizi:and if want end please enter 'end':\n")
		if posture=='end':
			exit(0)
		else:
			a=0
			s_jia_list=posture.split("+")
			for i in s_jia_list:
				a=a+jianfunc(i)
			print posture+'='+`a`
	except:
		print "you enter is error,like (1+2-3*...n)!\n"

