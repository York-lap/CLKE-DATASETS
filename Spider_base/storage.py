# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     storage
   Description :    负责将解析后的数据存储到数据库、文件或其他存储介质中。
   Author :       yk
   date：          2024/9/20
-------------------------------------------------
"""
import json


class Storage:
    def save_data(self, data, filename):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"数据已成功保存到 {filename}")
        except Exception as e:
            print(f"保存数据到 {filename} 时发生错误: {e}")