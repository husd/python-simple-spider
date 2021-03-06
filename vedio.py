#!/usr/bin/python
# coding=utf-8
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re

# -----------------------需要修改的参数----------------------
# _url = "https://github.com/search?q=%2A.properties+mail%3D%5B%5Cs%5D%2A%40%5Cs.com&ref=searchresults&type=Code&utf8=%E2%9C%93"
_url = "http://www.ka7g.com"
_t_file = "1.lst"
_cookie = ""
_data = ""
_timeout_second = 3
# -----------------------需要修改的参数----------------------

_u_agent_chrome = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"


def analysis_page_data(_page_data):
    soup = BeautifulSoup(_page_data, 'html.parser')
    print(soup.contents)
    td_list = soup.select('.code-list td')


def find_email():
    for _p in range(1, 3):
        _target_url = _url + "&p=" + str(_p)
        print("[+] reading ..." + str(_p) + " target url:" + _target_url)
        resp = _chrome(_target_url)
        if resp is not None and resp.status_code == 200:
            analysis_page_data(resp.text)
        else:
            print(resp)
            print("fail....")


def _chrome(target_url):
    return _open_url(target_url, _cookie, _data, _u_agent_chrome)


def _open_url(target_url, expect_cookie, expect_data, expect_agent):
    _host = urlparse(target_url).netloc
    headers = {'User-Agent': expect_agent, "Host": _host, "Cookie": expect_cookie, "Referer": _host}
    try:
        resp = requests.get(target_url, headers, timeout=_timeout_second, data=expect_data)
        return resp
    except Exception:
        pass


# def _find_host_from_url(_url):
#     o = urlparse(_url)
#     return o.netloc
# return re.search('(http://|https://)?w{0,3}([^/]*)',_url)

if __name__ == "__main__":
    find_email()
