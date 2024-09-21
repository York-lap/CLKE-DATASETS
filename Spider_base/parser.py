# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     parser
   Description :负责从响应中提取需要的数据
   Author :       yk
   date：          2024/9/20
-------------------------------------------------
"""
from bs4 import BeautifulSoup

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup