#!/usr/bin/env python
# coding=utf-8

import logging
import logging.handlers
import os


if not os.path.exists("log"):
    os.mkdir("log")

fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
formatter = logging.Formatter(fmt)   # 实例化formatter

# error log
ERROR_LOG_FILE = 'log/log.error'
error_handler = logging.handlers.RotatingFileHandler(ERROR_LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
error_handler.setFormatter(formatter)
error_logger = logging.getLogger('error')
error_logger.addHandler(error_handler)
error_logger.setLevel(logging.DEBUG)
ERROR_LOG = error_logger.error

# info log
INFO_LOG_FILE = 'log/log.info'
info_handler = logging.handlers.RotatingFileHandler(INFO_LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
info_handler.setFormatter(formatter)      # 为handler添加formatter
info_logger = logging.getLogger('info')    # 获取名为tst的logger
info_logger.addHandler(info_handler)           # 为logger添加handler
info_logger.setLevel(logging.DEBUG)
INFO_LOG = info_logger.info

# debug log
DEBUG_LOG_FILE = 'log/log.debug'
debug_handler = logging.handlers.RotatingFileHandler(DEBUG_LOG_FILE, maxBytes = 1024*1024, backupCount = 5) # 实例化handler
debug_handler.setFormatter(formatter)      # 为handler添加formatter
debug_logger = logging.getLogger('debug')    # 获取名为tst的logger
debug_logger.addHandler(debug_handler)           # 为logger添加handler
debug_logger.setLevel(logging.DEBUG)
DEBUG_LOG = debug_logger.debug