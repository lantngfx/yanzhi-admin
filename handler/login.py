#!/usr/bin/python
# -*- coding:utf8 -*-

import tornado.web
import json
import hashlib
from model.admin_model import admin_model_instance
from util.logger import *


class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        # 跨域处理
        self.set_header("Access-Control-Allow-Origin", "*")
        self.set_header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept")
        # 获取参数
        admin_name = self.get_argument('admin_name', '').strip()
        admin_passwd = self.get_argument('admin_passwd', '').strip()

        # 验证参数是否合法
        if not admin_name:
            ERROR_LOG('invalid param admin_name[%s]' % admin_name)
            self.write(json.dumps({"error_no": 1, "error_msg": "invalid param admin_name"}))
            return
        if not admin_passwd:
            ERROR_LOG('invalid param admin_passwd[%s]' % admin_passwd)
            self.write(json.dumps({"error_no": 1, "error_msg": "invalid param admin_passwd"}))
            return

        # 将密码加密
        admin_passwd = hashlib.md5(admin_passwd).hexdigest()
        admin_meta = admin_model_instance.login(admin_name, admin_passwd)
        if not admin_meta:
            ERROR_LOG('login fail admin_name[%s]' % admin_name)
            self.write(json.dumps({"error_no": -1, "error_msg": "login fail"}))
            return

        # 响应
        admin = {"admin_id": admin_meta.admin_id, "admin_name": admin_meta.name, "phone": admin_meta.phone}
        res = {"error_no": 0, "admin": admin}
        self.write(json.dumps(res))