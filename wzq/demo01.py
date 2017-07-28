#!/usr/bin/env python
# -*- coding:utf-8 -*-


#求两个数的最小公倍数

num1=num2=0
while(num1<1 or num2<1):
	try:	
		print("输入有误，请重新输入")
		num1=int(input("first number:"))
		num2=int(input("second number:"))
	except:
		pass
		
def xxx(x,y):
	for i in range(1,x*y):
		if (i%x==0 and i%y==0):
			return i
	
	return x*y	
			

print("xxx=",xxx(num1,num2))