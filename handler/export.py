#!/usr/bin/python
# -*- coding:utf8 -*-

import tornado.web
import json

class ExportHandler(tornado.web.RequestHandler):
    def get(self):
        # 跨域处理
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        # 假数据
        self.write(json.dumps({"error_no": 0, "down_url": ""}))
        return