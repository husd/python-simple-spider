#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import queue
import re
from urllib import request

from bs4 import BeautifulSoup

__author__ = 'hushengdong'

# @Date    : 2015-09-01 16:21:29
# @Author  : hushengdong (hu.shengdong.h@gmail.com)
# @Link    : 
# @Version : 1.0


logging.basicConfig(level=logging.INFO)

# 这个参数是需要查找的URL地址
__target_url = "http://www.jd.com"
# 记录下要抓取网站的长度
__target_url_len = len(__target_url)

# 最终找到的所有的URL的数量
__all_count = 0

# 需要忽略的URL
__ignore_dict = (
    '＃', 'javascript:;', 'javascript:', 'javascript', 'javascript:void(0)', 'javascript:void()', 'tel:400-010-0666')

# 这个是已经抓取过的URL缓存，每次抓取一个页面，就把这个URL放到缓存中去，防止重复抓取
# 先抓取这个站点的URL，如果不是本站，就不抓取，即不访问外站的URL
__url_cache = set()

# LBS算法队列
__url_to_deal_queue = queue.Queue()

# ajax请求列表
__ajax_url_ = []


# 这个是程序的入口代码，开始从起始页面抓起，
def spider_start_work():
    global __url_cache
    global __url_to_deal_queue
    __url_to_deal_queue.put(__target_url)
    while not __url_to_deal_queue.empty():
        __current_url = __url_to_deal_queue.get()
        if __current_url in __url_cache:
            # print('pass:',__current_url)
            pass
        else:
            skip_url = 'http://m.baojia.com/list'
            skip_url_brand = 'http://m.baojia.com/brand'
            if skip_url in __current_url or skip_url_brand in __current_url:
                print(__current_url)
                find_target_url(__current_url)
                __url_cache.add(__current_url)
            else:
                print(__current_url)
                find_target_url(__current_url)
                __url_cache.add(__current_url)


# 抓取页面方法
def find_target_url(current_url):
    # logging.info('find target url: %s ' % target_url_)
    with request.urlopen(current_url, ) as page_data:
        server_status = page_data.status
        server_reason = page_data.reason
        if server_status != 200 or server_reason != 'OK':
            logging.info(u"target url [{0:s}]unreachable server_status is {1:s} server_reason is {2:s}"
                         .format(current_url, server_status, server_reason))
            pass
        else:
            current_page_data = page_data.read()
            if current_url[-3:] == '.js':
                # find_current_page_js(current_page_data)
                pass
            else:
                find_current_page_url(current_page_data)


def encode_url_param(__current_url):
    skip_url = 'http://m.baojia.com/list'
    skip_url_len = len(skip_url)
    if __current_url[:skip_url_len] == skip_url:
        return skip_url + '/beijing'
    else:
        return __current_url


def find_current_page_js(current_page_data):
    current_page_data = current_page_data.decode('utf-8')
    cond = re.compile(r'^href=\"[^\"]+')
    _list = cond.findall(current_page_data)
    for i in _list:
        current_url = i[6:]
        add_to_queue(current_url)

    cond_2 = re.compile(r'url:\s?\"[/\w]+')
    list_2 = cond_2.findall(current_page_data)
    for i in list_2:
        current_url = i[6:]
        # ajax请求只记录下来链接，而不去抓取这个url
        logging.info('__ajax_url_:%s' % current_url)


def add_to_queue(current_url):
    global __url_to_deal_queue
    if is_url_need_to_record(current_url):
        if current_url[0] == "/":
            current_url = __target_url + current_url
        __url_to_deal_queue.put(current_url)


# 分析页面，查找当前页面所有的URL出来
def find_current_page_url(home_page_data):
    # logging.info('find_current_page_url start ...')
    soup = BeautifulSoup(home_page_data, 'html.parser')

    # 找到A标签里面的链接
    a_list = soup.find_all('a')
    for a_link in a_list:
        a_link_url = a_link.get('href')
        add_to_queue(a_link_url)

        # 找到ajax里面的链接
        # script_list=soup.find_all('script')
        # for script_temp in script_list:
        # 	script_src = script_temp.get('src')
        # 	add_to_queue(script_src)


# 判断URL是否需要被记录分析，如果不需要记录分析就返回False
# 如果需要分析就返回True
def is_url_need_to_record(target_url_):
    if target_url_ is None:
        return False
    if target_url_.isspace():
        return False
    len_1 = len('javascript')
    if target_url_[:len_1] == 'javascript':
        return False
    if target_url_[0] == '/':
        return True
    if target_url_ in __ignore_dict:
        return False
    skip_url = 'http://m.baojia.com/list'
    if skip_url in target_url_:
        return False
    if 'jquery' in target_url_:
        return False
    if 'jQuery' in target_url_:
        return False
    if 'amazeui' in target_url_:
        return False
    global __target_url_len
    if target_url_[0:__target_url_len] == __target_url:
        return True
    else:
        # logging.info('out side web site url:%s' % target_url_)
        return False


# 判断网站是否允许我们抓取它的页面，如果不允许，则返回False
# 详情请查看网站的rebots.txt文件
def check_target_permission():
    return True


# 程序入口代码
if __name__ == '__main__':
    permission_or_not = check_target_permission()
    if permission_or_not:
        spider_start_work()
        logging.info('find all url from [%s] end ,all count =%d' % (__target_url, __all_count))
    else:
        logging.info('find all url from [%s] interrupted ,permission deny!' % __target_url)
