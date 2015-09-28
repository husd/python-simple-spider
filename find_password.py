#!/usr/bin/python
#coding=utf-8

import os

#list all the files in specify absolute path
def list_files(path_name):
	for dir_path,dir_names,file_names in os.walk(path_name):
		for temp_file_name in file_names:
			if '密码' in temp_file_name:
				print('found : %s ' % temp_file_name)


if __name__ == '__main__':
	list_files("/Users/hushengdong/")