#!/usr/bin/python
#codeing=utf-8

def fact(x):
	return x > 1 and x * fact(x-1) or 1

for i in range(1,20):
	print(fact(i))