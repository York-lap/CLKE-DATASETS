# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     logger
   Description :负责记录爬虫运行过程中的日志信息。
   Author :       yk
   date：          2024/9/20
-------------------------------------------------
"""
import logging

import logging

def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('spider_log.log')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger