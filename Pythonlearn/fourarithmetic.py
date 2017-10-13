#!/usr/bin/python
stringss=raw_input("Please enter the shizi:\n")
strings=stringss+'+'
print strings
gl_i=0
sum=0
num1=0
nums1=''
num=0
flog=''
while gl_i<len(strings):
	if strings[gl_i] in ['1','2','3','4','5','6','7','8','9','0']:
		nums1=nums1+strings[gl_i]
	elif strings[gl_i]=='+':
		num1=int(nums1)
		if num==0:
			sum=sum+num1
		else:
			if flog=='*':
				sum=sum+num*num1
			else:
				sum=sum+num/num1
			num=0
		nums1=''
	elif strings[gl_i]=='*':
		flog='*'
		if num==0:
			num=int(nums1)
		else:
			num=num*int(nums1)
		nums1=''
	else:
		flog=r'/'
		if num==0:
			num=int(nums1)
		else:
			num=num/int(nums1)
		nums1=''
	gl_i=gl_i+1
print sum

