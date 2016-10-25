#!/usr/bin/python
# coding=utf-8
import crypt
import sys

#-------字典文件和密码文件
_dict = "/Users/hushengdong/script/dict/dict1.txt"
_password_f = "/etc/passwd"
#-------字典文件和密码文件

def _f():
    _temp = line.split(":")
    salt = _temp[1][0:2]
    with open(_dict, 'r') as f1:
        for _line in f1.readlines():
            _line = line.strip("\n")
            crypt_line = crypt.crypt(_line, salt)
            if _temp[1] == crypt_line:
                print("[+] password found:{0} user:{1}".format(_line, _temp[0]))
                return
        print("[-] password not found:" + _temp[0])


if __name__ == "__main__":
    print(sys.argv)
    with open(_password_f, 'r') as f:
        for line in f.readlines():
            if ":" in line:
                _f()
