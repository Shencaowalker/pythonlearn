def haha(sg,x,y):
	try:
		while sg[x]==sg[y]:
			y=y+1
			x=x-1
		else:
			return False
		return True
	except:
		return True



def is_pal(n):
	n=str(n)
	if len(n)==1:
		return True
	else:
		num=len(n)/2
		if len(n)%2==0:	
			haha(n,num-1,num)
		else:
			haha(n,num-1,num+1)


if __name__=="__main__":
	a=''
	while a !='end':	
		a=raw_input(":")
		if is_pal(a):
			print "Yes"







