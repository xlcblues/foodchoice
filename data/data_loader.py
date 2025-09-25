import os
from pathlib import Path

# 获取食物数据
def load_food_data():
    # 数据准备
    if not os.path.exists("file.txt"):
        Path.touch("file.txt")

    # 读取文件
    with open('file.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        food = content.split()
        return food
