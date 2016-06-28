#!/usr/bin/python
# coding=utf-8
import urllib.request
import urllib.response
import re

def open_with_chrome(_url):
    _host = re.search('(http://|https://)?w{0,3}([^/]*)',_url)
    _cookie = ""
    try:
        resp = _o_chrome(_url,_host.group(),_cookie)
        print(_url + " status:" + str(resp.status) + " reason:" + resp.reason)
    except ValueError:
        print(_url + " error")

def _o_chrome(_url,_host,_cookie):
    req = urllib.request.Request(_url)
    req.add_header("User-Agent:","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36")
    req.add_header("Host",_host)
    req.add_header("Cookie",_cookie)
    req.add_header("Referer",_host)
    resp = urllib.request.urlopen(_url)
    return resp

if __name__ == "__main__":
    open_with_chrome("http://www.hushengdong.com/")
