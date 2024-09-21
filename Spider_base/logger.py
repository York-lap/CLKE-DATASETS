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

def setup_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    return logger