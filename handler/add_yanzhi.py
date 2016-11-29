#!/usr/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import json


class AddYanzhiHandler(tornado.web.RequestHandler):
    def options(self):
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        self.write(json.dumps({"error_no": 0}))

    def post(self):
        # 跨域处理
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        self.set_header('Access-Control-Allow-Methods', 'POST, GET, OPTIONS')
        # 假数据
        self.write(json.dumps({"error_no": 0}))
        return