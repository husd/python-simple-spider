#!/usr/bin/python
# coding=utf-8
import requests
from urllib.parse import urlparse

# -----------------------需要修改的参数----------------------
_url = "http://www.hushengdong.com/"
_cookie = ""
_data = ""
_timeout_second = 3
# -----------------------需要修改的参数----------------------

_u_agent_chrome = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"


def open_with_chrome():
    try:
        resp = _chrome(_url)
        print(_url + " status:" + str(resp.status_code) + " reason:" + resp.reason)
    except ValueError:
        print(_url + " error")


def _chrome(target_url):
    return _open_url(target_url, _cookie, _data, _u_agent_chrome)


def _open_url(target_url, expect_cookie, expect_data, expect_agent):
    _host = urlparse(target_url).netloc
    headers = {'User-Agent': expect_agent, "Host": _host, "Cookie": expect_cookie, "Referer": _host}
    resp = requests.get(target_url, headers, timeout=_timeout_second, data=expect_data)
    return resp


# def _find_host_from_url(_url):
#     o = urlparse(_url)
#     return o.netloc
# return re.search('(http://|https://)?w{0,3}([^/]*)',_url)

if __name__ == "__main__":
    open_with_chrome()
