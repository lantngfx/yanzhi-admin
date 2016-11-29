#!/usr/bin/env python
# -*- coding:utf8 -*-

import tornado.web
import json
import hashlib
from tornado.escape import json_decode

from model.admin_model import admin_model_instance
from util.logger import *


class UpdatePwdHandler(tornado.web.RequestHandler):
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

        # 获取参数
        try:
            param_dict = json_decode(self.request.body)
        except Exception, e:
            ERROR_LOG('get param has error[%s]' % e)
            self.write(json.dumps({"error_no": 1, "error_msg": "param should be json"}))
            return

        if not param_dict.has_key('old_password') or not param_dict['old_password']:
            ERROR_LOG('param old_password invalid')
            self.write(json.dumps({"error_no": 1, "error_msg": "param old_password invalid"}))
            return

        if not param_dict.has_key('new_password') or not param_dict['new_password']:
            ERROR_LOG('param new_password invalid')
            self.write(json.dumps({"error_no": 1, "error_msg": "param new_password invalid"}))
            return

        if not param_dict.has_key('admin_name') or not param_dict['admin_name']:
            ERROR_LOG('param admin_name invalid')
            self.write(json.dumps({"error_no": 1, "error_msg": "param admin_name invalid"}))
            return
        admin_name = param_dict['admin_name']
        old_password = param_dict['old_password']
        new_password = param_dict['new_password']

        # 将密码转换成加密
        admin_password = hashlib.md5(old_password).hexdigest()
        admin_meta = admin_model_instance.login(admin_name, admin_password)

        if not admin_meta:
            self.write(json.dumps({"error_no": -1, "error_msg": "the old_pwd is error"}))
            return
        admin_id = admin_meta.admin_id
        new_password = hashlib.md5(new_password).hexdigest()
        sql = "update admin set passwd='%s' where admin_id = '%s'" % (new_password, admin_id)
        if admin_model_instance.update_pwd(sql):
            self.write(json.dumps({"error_no": 0}))
        else:
            self.write(json.dumps({"error_no": -1, "error_msg": "update passwd fail"}))

