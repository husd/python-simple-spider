#!/usr/bin/python
# coding=utf-8

import math


def test_input():
    input_str = input('input some number :')
    input_int = int(input_str)
    if input_int < 1000:
        print('less then 1000')
    else:
        print('more then 1000')


def test_init_list():
    list_init = list(range(0, 10))
    print(list_init)


'''

	这个方法有多个返回值，通过测试可以发现，实际返回的是一个不可变的truple
	在使用返回值的时候，也需要接收所有的参数才行：

	x,y,z=test_move_point(10,20,3,0)

	像下面这个调用就不正确：
	x,y=test_move_point(10,20,3,0)

	少接收了一个参数

	注意：返回值不可变

'''


def test_move_point(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    # 如果函数没有返回值的话，那么就会默认执行
    # return None
    return nx, ny, 1


'''

严格讲不算一个可变参数的例子，只不过是把一个list传递进去了，
在使用这个方法的时候，也只是把多个参数封装起来，当作一个参数传递进去，

更合适的写法见下面一个函数: {@code test_variable_arguments_2(*numbers)}

'''


def test_variable_arguments(numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum


'''
这个方法可以传入可变参数，例如：

test_variable_arguments_2(1,3,4,5)

如果已经有一个list了，想传入一个list ,就要加上一个＊，例：
test_list=[1,2,34,5,6]
test_variable_arguments_2(*test_list)

'''


def test_variable_arguments_2(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum


# 不受限制，可以任意传入的关键字参数
def test_key_word_argument(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)


# 限制传入的关键字参数名称
'''

 		这个是关键字参数的用法，除了必须的2个参数name age之外，这个方法还允许
 	接收其它的关键字参数，例如：city='beijing',job='engineer'

 		和上一个方法: test_key_word_argument(name,age,*kw)不同的是，
 	前者对关键字参数的名称没有明确的限制，可以随意传入，而这个方法
 	限制了关键字参数的名称，不可以传入其它关键字。

 	使用命名关键字参数时，要特别注意，*不是参数，而是特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数
 	def test_normal_argument(name,age,city,job):
 		#缺少了＊，那么city job会被认为位置参数
 		print(name,age,city,job)

 		有时候自由是有代价的，如果过度自由，就会增加出错的风险，适当的加以限制，
 	就可以减少风险，辩证主义的观点。


'''


def test_key_word_special_argument(name, age, *, city, job):
    print(name, age, city, job)


'''
	这个方法是默认参数的声明

	但是如这个方法就有问题：

		def add_end(L=[]):
			L.append('end')
			return L

	Python函数在定义的时候，默认参数L的值就被计算出来了，
	即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
	如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。

	默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误

	修复方法:

		def add_end(L=None):
			if L is None:
				L=[]
			L.append('end')
			return L

	这样方法每次调用的时候，就不会返回函数声明的时候指向的那个L了，而是在方法内
	重新生成的那个空链接 : L=[]

'''


def test_default_argument(name, age, city='beijing'):
    print(name, age, city)


if __name__ == "__main__":
    # test_input()
    test_init_list()
    x, y, z = test_move_point(100, 100, 60, math.pi / 6)
    print('x is %s ' % x)
    print('y is %s ' % y)
    print('z is %s ' % z)
    r = test_move_point(100, 100, 60, math.pi / 6)
    # 函数可以同时返回多个值，但其实就是一个tuple。
    print(r)

    # 可变参数
    numbers = [1, 2, 3, 4, 5]
    numbers_resp = test_variable_arguments(numbers)
    print(numbers_resp)

    print(test_variable_arguments_2(1, 2, 3))
    print(test_variable_arguments_2(*numbers))

    # 下面这种调用方法是不正确的
    # 对于多参数的调用，需要加上*，方法才能接收
    # print(test_variable_arguments_2(numbers))

    test_key_word_argument('husd', 20, city='beijing')

    test_default_argument('husd', 20)
    test_default_argument('husd', 20, 'shanghai')
