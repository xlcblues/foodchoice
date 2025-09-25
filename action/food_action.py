import random

from data import data_loader
from tkinter import messagebox

class FoodSelector:
    def __init__(self):
        self.food_list = data_loader.load_food_data()

    # 选择食物
    def select_food(self):
        print(random.choice(self.food_list))
        return random.choice(self.food_list)

    # 显示选择结果
    def show_selection(self):
        selected_food = self.select_food()
        messagebox.showinfo(
            "命运的选择是",  # 弹窗标题
            f"命运的选择是：{selected_food}"  # 弹窗内容
        )
        return selected_food