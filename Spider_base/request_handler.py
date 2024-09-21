# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     request_handler
   Description :
   Author :       yk
   date：          2024/9/20
-------------------------------------------------
"""
import requests


def send_request(url, headers=None, params=None):
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"请求出错：{e}")
        return None
