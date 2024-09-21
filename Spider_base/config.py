# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     config
   Description :存放爬虫的各种配置信息，如数据库连接信息、
                目标网站URL、请求头等。
   Author :       yk
   date：          2024/9/20
-------------------------------------------------
"""
import random

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15",
    # 添加更多的 User-Agent 字符串
]

REQUEST_HEADERS = {
    'User-Agent': random.choice(user_agents)
}