#!/usr/bin/python
#coding=utf-8


#单词用空格来分开，这个不能适用所用的
#情况
def word_count(file_name):
	count=0
	with open(file_name,'r') as f:
		for line in f.readlines():
			words=line.split(' ')
			print(words)
			count=count+len(words)
	return count

if __name__ == '__main__':
	file_name='test_file.py'
	count=word_count(file_name)
	print('count= %s' % count)
	print(1)