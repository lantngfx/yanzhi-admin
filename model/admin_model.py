#!/usr/bin/python
# -*- coding:utf8 -*-

from util.logger import *
from util.db_conf import *

class AdminMeta:
    def __init__(self, meta):
        self.admin_id = meta.admin_id
        self.name = meta.name
        self.passwd = meta.passwd
        self.phone = meta.phone
        self.email = meta.email
        self.status = meta.status
        self.updatetime = meta.updatetime

class AdminModel:
    def login(self, admin_name, admin_passwd):
        sql = "select * from admin where name='%s' and passwd='%s'" % (admin_name, admin_passwd)
        try:
            admin = db_conn.get(sql)
        except Exception, e:
            ERROR_LOG('select table admin has error[%s]' % e)
            return
        if admin:
            return AdminMeta(admin)

    def update_pwd(self, sql):
        try:
            db_conn.update(sql)
        except Exception, e:
            ERROR_LOG('update admin has error[%s].sql[%s]' % (e, sql))
            return
        return 1
admin_model_instance = AdminModel()