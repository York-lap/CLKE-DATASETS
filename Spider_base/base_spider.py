# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     base_spider
   Description :爬虫基类，这些基类包含所有爬虫共通的属性和方法，
                如初始化方法、请求发送、响应处理、数据解析等。
   Author :       yk
   date：          2024/9/20
-------------------------------------------------
"""
from .config import REQUEST_HEADERS
from .logger import setup_logger
from .request_handler import send_request
from .response_handler import handle_response
from .storage import Storage
from .parser import parse_html
from .utils import utility_function


class BaseSpider:
    def __init__(self):
        self.config = None
        self.logger = None
        self.request_handler = None
        self.response_handler = None
        self.storage = None
        self.parser = None
        self.utils = None

    def setup(self):
        # 初始化各个模块

        self.config = {
            'request_headers': REQUEST_HEADERS
        }
        self.logger = self.setup_logger()
        self.request_handler = self.setup_request_handler()
        self.response_handler = self.setup_response_handler()
        self.storage = self.setup_storage()
        self.parser = self.setup_parser()
        self.utils = self.setup_utils()

    def setup_logger(self):
        return setup_logger()

    def setup_request_handler(self):
        return send_request

    def setup_response_handler(self):
        return handle_response

    def setup_storage(self):
        return Storage()

    def setup_parser(self):
        return parse_html

    def setup_utils(self):
        return utility_function