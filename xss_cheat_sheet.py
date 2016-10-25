#!/usr/bin/python
# coding=utf-8
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

# -----------------------需要修改的参数----------------------
_url = "https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet#XSS_Locator"
_t_file = "xss_cheat_sheet.lst"
_select_item = 'pre'
_cookie = ""
_data = ""
_timeout_second = 3
# -----------------------需要修改的参数----------------------

_u_agent_chrome = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"


def _append_to_file(_td_list):
    with open(_t_file, 'a+') as f:
        for _td in _td_list:
            _td_text = _td.get_text()
            try:
                f.write(_td_text)
            except Exception:
                pass


def analysis_page_data(_page_data):
    soup = BeautifulSoup(_page_data, 'html.parser')
    td_list = soup.select(_select_item)
    _append_to_file(td_list)


def _f_target():
    _target_url = _url
    resp = _chrome(_target_url)
    analysis_page_data(resp.text)


def open_with_chrome():
    try:
        resp = _chrome(_url)
        print(_url + " status:" + str(resp.status_code) + " reason:" + resp.reason)
        return resp
    except ValueError:
        print(_url + " error")


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
    _f_target()
