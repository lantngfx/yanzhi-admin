#!/usr/bin/python
# -*- coding:utf8 -*-

import tornado.web
import json

class YanzhiDetailListHandler(tornado.web.RequestHandler):
    def get(self):
        # 跨域处理
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        # 假数据
        total_number = 1000
        data1 = {"id": "00005f89cce3aee669607a60f5cbd59b", "uid": "6c0e2f4e0f7d9151c9e4a9c298302235", "op_type": "第一次使用APP", "obj_title": "", "create_time": "2016-10-17", "op_value": 2}
        data2 = {"id": "0001725bbc9a59d0956612caef8d533c", "uid": "0d1426ef9d4308f60b2d1937e738ddd4", "op_type": "分享文章", "obj_title": "善友：社群的力量超乎想象 得弱关系得天下", "create_time": "2016-10-17", "op_value": 1}
        data3 = {"id": "0007a480020e8b4568b584a7c0738d6a", "uid": "1dc266d98634d4a36493bf0c25764b3b", "op_type": "分享APP", "obj_title": "", "create_time": "2016-10-18", "op_value": 2}
        data4 = {"id": "00073edd23cecb72a0fdd22ce6f3a579", "uid": "8cc9f9e61e46389b6782cbd9685ba523", "op_type": "完善个人资料", "obj_title": "", "create_time": "2016-10-18", "op_value": 2}
        data5 = {"id": "00079748dbd9d3bb4f713e62f25b6509", "uid": "5943efcd4951629f6e4a3c51d336cc94", "op_type": "完成微作业", "obj_title": "", "create_time": "2016-10-13", "op_value": 2}
        data6 = {"id": "0000196f527035f873c9a70f789ea866", "uid": "a9bf2aceabf3613637d52132bd28a524", "op_type": "分享文章", "obj_title": "李善友：微信和QQ、OPPO和VIVO，内部竞争不是资源浪费【笔记】", "create_time": "2016-10-21", "op_value": 1}
        data = [data1, data2, data3, data4, data5, data6]
        res = {"error_no": 0, "detail_list": data, "total_number": total_number}
        self.write(json.dumps(res))
        return