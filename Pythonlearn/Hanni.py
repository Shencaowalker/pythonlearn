#!/usr/bin/python

def move(n,a,b,c):
	if n==1:
		end_move(n,a,b)
	else:
		move(n-1,a,c,b)
		end_move(n,a,b)
		move(n-1,c,b,a)


def end_move(n,a,b):
	print "%s===>%s" %(a,b)


num=int(raw_input("Please enter n:\n"))
a="A"
b="B"
c="C"
move(num,a,b,c)

