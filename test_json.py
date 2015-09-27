#!/usr/bin/python
#coding=utf-8

#python内置的json可以方便的在python和json之间进行转换
import json

#
# python对象和json对应的关系
# 
# JSON类型		PYTHON类型
#
#	{}		 	dict
#	[]		 	list
#	"string"  	'str'or u'unicode'
#	true/false	 True/False
#	null		Null
#
#

class Student(object):

	def __init__(self,name,age,score):
		self.name=name
		self.age=age
		self.score=score


def student2dict(std):
	return{
		'name':std.name,
		'age':std.age,
		'score':std.score
	}

def dict2student(dict):
	return Student(dict['name'], dict['age'], dict['score'])

#把一个json转换为python对象
def test_json_to_python():
	d=dict(name='husd',age=12,sex=1)
	d_json=json.dumps(d)
	print('json format of d is %s ' % d_json)

	s=Student('husd', 20, 80)
	student_json=json.dumps(s,default=student2dict)
	print('stduent json is :' + student_json)
	pass

#把一个python对象转换为json
def test_python_to_json():
	json_str = '{"age": 20, "score": 88, "name": "Bob"}'
	python_ob=json.loads(json_str)
	print('dict start ...')
	print(python_ob['age'])
	print(python_ob['score'])
	print(python_ob['name'])
	print('dict end...')

	print('dict to python object ')
	#这个是把json对象转换为python对象，需要定义一个函数来转换这个对象
	student_test=json.loads(json_str,object_hook=dict2student)
	print('student_test is : \n')
	print(student_test.name)
	pass




if __name__ == '__main__':
	print('test json operation in python start ....')
	test_json_to_python()
	test_python_to_json()
	print('test json operation in python end....')