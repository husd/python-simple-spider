#!/usr/bin/python
#coding=utf-8

'''
	快速生成一个列表

'''
def test_fast_list():
	return list(range(0,11))

def test_fast_power():
	l=[]
	for i in range(0,11):
		l.append(i*i)
	return l

'''

	这个方法的写法是上面方法：test_fast_power()
	的一种简单写法，应该是python的一种语法糖

'''
def test_faster_power():
	return [i*i for i in range(0,11)]

if __name__ == '__main__':
	print(test_fast_list())
	print(test_fast_power())
	print(test_faster_power())