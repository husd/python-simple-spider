#!/usr/bin/python
# coding=utf-8

import sys
import base64 as _b64


def _decode(_s):
    """

    :rtype: object
    """
    try:
        a = _b64.b64decode(_s)
        _s_a = str(a)
        print("[" + _s + "] decode by base64:" + _s_a)
        return _s_a
    except Exception:
        print("[" + _s + "] decode by base64 error:")
        return ""


def _info():
    """

    :rtype: object
    """
    print(" 请指定需要使用base64解码的字符串 : python b64_decode.py 'str you want to decode by base64' \n python b64_decode.py 'YWJjZGU=' will display [abcde] encode by base64:b'YWJjZGU=' ")


if __name__ == "__main__":
    if len(sys.argv) == 1:
        _info()
    else:
        _decode(sys.argv[1])
