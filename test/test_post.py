#!/usr/bin/python
# -*- coding: utf8 -*-

import urllib
import json

def main():
    url = 'http://localhost:9105/yanzhi-admin/update_password'
    param_dict = {"admin_name": "娄永锋", "old_password": "123", "new_password": "125"}
    res = urllib.urlopen(url, json.dumps(param_dict)).read()
    print res


def get_url():
    time_list = ['32:00', '32:08', '32:07', '38:21', '28:59', '30:43']
    for r in time_list:
        mi, sec = r.split(':')
        print int(mi) * 60 + int(sec)


if __name__ == '__main__':
    main()

