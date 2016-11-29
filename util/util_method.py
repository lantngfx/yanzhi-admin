#!/usr/bin/python
# -*- coding:utf8 -*-

from util.logger import *

def get_state(course_state):
    import types
    if type(course_state) is types.IntType or type(course_state) is types.LongType:
        state_list = [0b0000001, 0b0000010, 0b0000100, 0b0001000, 0b0010000, 0b0100000, 0b1000000]
        state_str = ['预告', '报名中', '即将直播', '直播中', '直播结束', '回放', '购买可见']
        curr_state = []
        for num in range(7):
            if course_state & state_list[num]:
                curr_state.append(state_str[num])
        return ' '.join(curr_state)
    else:
        state_dict = {u'预告': 1, u'报名中': 2, u'即将直播': 4, u'直播中': 8, u'直播结束': 16, u'回放': 32, u'购买可见': 64}
        if state_dict.has_key(course_state):
            return state_dict[course_state]
        else:
            ERROR_LOG('has error')


def get_type(key):
    # 课程类型的整数与字符串之间的转换
    int_str_dict = {0: '现场大课', 1: '线上小课', 100: '大课回放', 101: '精品课'}
    str_int_dict = {u'现场大课': 0, u'线上小课': 1, u'大课回放': 100, u'精品课': 101}
    if int_str_dict.has_key(key):
        return int_str_dict[key]
    elif str_int_dict.has_key(key):
        return str_int_dict[key]
    else:
        ERROR_LOG('the type is invalid type[%s]' % key)
        return 100

def get_status(key):
    # 课程类型的整数与字符串之间的转换
    int_str_dict = {0: '隐藏', 1: '显示'}
    str_int_dict = {u'隐藏': 0, u'显示': 1}
    if int_str_dict.has_key(key):
        return int_str_dict[key]
    elif str_int_dict.has_key(key):
        return str_int_dict[key]
    else:
        ERROR_LOG('the type is invalid type[%s]' % key)

def get_only_yanzhi(key):
    # 课程类型的整数与字符串之间的转换
    int_str_dict = {0: '非研值', 1: '研值课'}
    str_int_dict = {u'非研值': 0, u'研值课': 1}
    if int_str_dict.has_key(key):
        return int_str_dict[key]
    elif str_int_dict.has_key(key):
        return str_int_dict[key]
    else:
        ERROR_LOG('the only_yanzhi is invalid only_yanzhi[%s]' % key)
