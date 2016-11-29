#!/usr/bin/python
# -*- coding:utf8 -*-

import tornado.web
import json

class GetRulesHandler(tornado.web.RequestHandler):
    def get(self):
        # 跨域处理
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        # 假数据
        data1 = {"id": "1", "name": "分享", "flag": "增加", "op_value": 1}
        data2 = {"id": "2", "name": "微作业", "flag": "增加", "op_value": 3}
        data3 = {"id": "3", "name": "邀请好友入社", "flag": "增加", "op_value": 50}
        data4 = {"id": "4", "name": "被邀请入社", "flag": "增加", "op_value": 5}
        data5 = {"id": "5", "name": "第一次使用APP", "flag": "增加", "op_value": 2}
        data6 = {"id": "6", "name": "完善个人资料", "flag": "增加", "op_value": 2}
        data = [data1, data2, data3, data4, data5, data6]
        res = {"error_no": 0, "data": data}
        self.write(json.dumps(res))
        return