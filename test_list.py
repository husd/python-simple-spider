#!/usr/bin/python
# coding=utf-8

from collections import Iterable

'''
	快速生成一个列表

'''


def test_fast_list():
    return list(range(0, 11))


def test_fast_power():
    l = []
    for i in range(0, 11):
        l.append(i * i)
    return l


'''

	这个方法的写法是上面方法：test_fast_power()
	的一种简单写法，应该是python的一种语法糖

'''


def test_faster_power():
    return [i * i for i in range(0, 11)]


'''
	
	对于dict的迭代，一般都是按key值来迭代，根据key值可以获取到value值
	由于dict的存储顺序不像list那样，遍历出来的顺序并不固定

'''


def test_iterator_dict():
    d = {'a': 1, 'b': 2, 'c': 3}
    for key in d:
        print(key, d[key])


# 遍历字典的value值
def test_iterator_dict_value():
    d = {'a': 1, 'b': 2, 'c': 3}
    print('字典是否可以遍历:', isinstance(d, Iterable))
    print('字符串是否可以遍历:', isinstance('abc', Iterable))
    print('数字是否可以遍历:', isinstance(1234, Iterable))
    for value in d.values():
        print(value)
    # 这种方式的遍历特别有用
    for k, v in enumerate(d):
        print(k, v)


'''
	
	通过列表生成式，我们可以直接创建一个列表。
	但是，受到内存限制，列表容量肯定是有限的。
	而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
	如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

	所以，如果列表元素可以按照某种算法推算出来，那我们是否可以在循环的过程中不断推算出后续的元素呢？
	这样就不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。

	转：http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014317799226173f45ce40636141b6abc8424e12b5fb27000

'''


def test_generator():
    # 普通的列表，运行时候会生成所有的数据，如果数据量特别大的话，会占
    # 用大量的内存,如果我们只需要其中一部分的数据，那么就会造成内存浪费
    L = [x * x for x in range(10)]
    print(L)

    # 生成器模式，一边用一边生成数据，数据量和你调用生成器的次数有关
    test_g = (x * x for x in range(10))
    print(next(test_g))
    print(next(test_g))
    for n in test_g:
        print(n)


'''
	
	交换a,b的值，究竟python里面的参数传递是值传递还是引用传递呢？
	return a,b究竟返回的是什么值呢？

'''


def test_swap(a, b):
    a, b = b, a
    return a, b


if __name__ == '__main__':
    print(test_fast_list())
    print(test_fast_power())
    print(test_faster_power())
    test_iterator_dict()
    test_iterator_dict_value()
    test_generator()
    a = 2
    b = 3
    a, b = test_swap(a, b)
    print(a, b)
