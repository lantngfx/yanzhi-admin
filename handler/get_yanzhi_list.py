#!/usr/bin/python
# -*- coding:utf8 -*-

import tornado.web
import json

class GetYanzhiListHandler(tornado.web.RequestHandler):
    def get(self):
        # 跨域处理
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        # 假数据
        total_number = 60
        user1 = {"uid": "0002871a0e48b940a74e761209a7dd82", "name": "张馨予", "nickname": "张馨予", "utype": "在线社员", "phone": "15998236505", "tp_type": "weixin", "yanzhi": 66}
        user2 = {"uid": "eb7a9356d600a42d621469a04ec77", "name": "collin", "nickname": "三横一竖", "utype": "在线社员", "phone": "13817833402", "tp_type": "weixin", "yanzhi": 103}
        user3 = {"uid": "000e3f3a8e7154e3459d2baa8a35d5da", "name": "孙雪峰", "nickname": "孙雪峰-(´ᴥ`)و", "utype": "铁杆社员", "phone": "13439237501", "tp_type": "qq", "yanzhi": 222}
        user4 = {"uid": "000e284f399234c36e8298b55c21c560", "name": "", "nickname": "[自强不息*厚德载物]", "utype": "注册用户", "phone": "", "tp_type": "qq", "yanzhi": 34}
        user5 = {"uid": "000c6e746a802e09f8f03187e5224361", "name": "", "nickname": "巴小花", "utype": "注册用户", "phone": "", "tp_type": "weixin", "yanzhi": 77}
        user6 = {"uid": "000ba495d7ffe47fa13f3fc2a8ef9fa1", "name": "程阿琴", "nickname": "阿琴", "utype": "在线社员", "phone": "13718070797", "tp_type": "weixin", "yanzhi": 345}
        user_list = [user1, user2, user3, user4, user5, user6]
        res = {"error_no": 0, "user_list": user_list, "total_number": total_number}
        self.write(json.dumps(res))
        return