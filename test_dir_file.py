#!/usr/bin/python
#coding=utf-8

import os

#list all the files in specify absolute path
def list_files(path_name):
	for dir_path,dir_names,file_names in os.walk(path_name):
		for temp_file_name in file_names:
			#print(temp_file_name)
			pass

def list_path_order():
	#获取系统名称
	print(os.name)
	#获取系统的属性
	print(os.uname())
	#获取某一个环境变量
	print(os.getenv("PATH"))
	#print(os.environ)
	print(os.path.abspath('.'))
	#连接2个路径,可以正确的把2个路径组合为一个路径	
	print(os.path.join('a','b'))
	#同理，如果需要拆分路径，直接使用split函数
	test_url="/opt/wf/e.baojia.com/conf/activity.properties"
	test_url_list=os.path.split(test_url)
	print(test_url_list)
	test_file='/temp/test.txt'
	if os.path.exists(test_file) == False:
		print('file %s do not exist ' % test_file)
		pass
	print(os.rename('test_dir_file.py','a.py'))
	print(os.rename('a.py','test_dir_file.py'))

#遍历当前的目录，把所有的.py结尾的文件找出来并打印文件的名字
def show_all_file_in_path():
	for temp_file in os.listdir('.'):
		if os.path.isfile(temp_file) and os.path.splitext(temp_file)[1]=='.py':
			print(temp_file)
		else:
			pass

if __name__ == '__main__':
	list_files('/opt/wf/')
	temp=os.path.abspath('/opt/wf/logs')
	print(temp)
	list_path_order()
	show_all_file_in_path()
	str_test_in='58.txt'
	if '58' in str_test_in:
		print('58 in %s' % str_test_in)


