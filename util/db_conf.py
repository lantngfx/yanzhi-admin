#!/use/bin/python
# -*- coding=utf8 -*-

import torndb
from conf.mysql_conf import *

db_conn = torndb.Connection(host=db_conf['host'], user=db_conf['user'], password=db_conf['passwd'],
                            database=db_conf['db_name'])

