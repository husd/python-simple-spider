#!/usr/bin/python
# coding=utf-8

import sys
import base64 as _b64


def _encode(_s):
    """

    :rtype: object
    """
    try:
        a = _b64.b64encode(_s.encode('ascii'))
        _s_a = str(a)
        print("[" + _s + "] encode by base64:" + _s_a)
        return _s_a
    except Exception:
        print("[" + _s + "] encode by base64 error:")
        return ""


def _info():
    """

    :rtype: object
    """
    print(" 请指定需要使用base64编码的字符串 : python b64_encode.py 'str you want to encode by base64'")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        _info()
    else:
        _encode(sys.argv[1])
