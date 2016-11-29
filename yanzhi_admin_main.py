#!/usr/bin/python
# -*- coding: utf8 -*-

import sys
import getopt

reload(sys)
sys.setdefaultencoding('utf-8')


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from handler.login import *
from handler.update_pwd import *
from handler.get_yanzhi_list import *
from handler.export import *
from handler.add_yanzhi import *
from handler.get_rules import *
from handler.update_rule import *
from handler.update_picture import *
from handler.yanzhi_detail_list import *
from handler.update_detail import *


if __name__ == '__main__':
    app = tornado.web.Application(
        handlers=[
            # 登录接口
            (r'/yanzhi-admin/login', LoginHandler),
            (r'/yanzhi-admin/update_password', UpdatePwdHandler),
            (r'/yanzhi-admin/get_yanzhi_list', GetYanzhiListHandler),
            (r'/yanzhi-admin/export', ExportHandler),
            (r'/yanzhi-admin/add_yanzhi', AddYanzhiHandler),
            (r'/yanzhi-admin/get_rules', GetRulesHandler),
            (r'/yanzhi-admin/update-rule', UpdateRuleHandler),
            (r'/yanzhi-admin/update_picture', UpdatePictureHandler),
            (r'/yanzhi-admin/all_yanzhi_detail', YanzhiDetailListHandler),
            (r'/yanzhi-admin/update_detail', UpdateDetailHandler),
        ],
    )

    # 服务路由设置
    # 解析命令行参数
    listen_port = 9105
    opts, args = getopt.getopt(sys.argv[1:], 'p:', ['port='])
    for opt, arg in opts:
        if opt in ('-p', '--port'):
            listen_port = int(arg)

    # 启动web服务器 启动服务器
    define("port", default=listen_port, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


# http://192.168.70.74:8080/#!/login