#!/usr/bin/python
# -*- coding: utf8 -*-

# 数据库配置
flag = 'offline'

if flag == 'online':
    db_host = '10.44.45.122'
    db_port = 16033
else:
    db_host = '123.57.143.47'
    db_port = 3306
db_name = 'course'
db_pass = 'dever'
db_user = 'dever'

db_conf = {'host': '123.57.143.47:3306', 'user': 'dever', 'passwd': 'dever', 'db_name': 'yanzhi'}

