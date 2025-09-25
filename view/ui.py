from action.food_action import FoodSelector

import tkinter as tk

class FoodView:
    def __init__(self):
        self.selector = FoodSelector()
        self.root = tk.Tk()
        self.setup_ui()

    def setup_ui(self):
        self.root.geometry("800x600")
        self.root.title("今晚吃啥？")
        self.root.configure(bg='#F0F8FF')

        title = tk.Label(
            self.root,
            text="午餐选择困难症救星",
            fg="#FF6B6B",  # 珊瑚红色
            font=('微软雅黑', 36, 'bold'),
            bg='#F0F8FF'
        )
        title.pack(pady=40)

        # 图片占位符（实际项目中可替换为真实食物图片）
        self.image_label = tk.Label(
            self.root,
            text="🍔🍲🍕🍣",
            font=('Arial', 64),
            bg='#F0F8FF'
        )
        self.image_label.pack(pady=40)

        # 选择按钮
        select_btn = tk.Button(
            self.root,
            text="✨ 命运决定器 ✨",
            command=self.on_select_click,
            bg="#4CAF50",  # 绿色
            fg="white",
            font=('微软雅黑', 14, 'bold'),
            padx=20,
            pady=10,
            relief=tk.GROOVE
        )
        select_btn.pack(pady=(0, 20))

        # 状态标签
        self.status = tk.Label(
            self.root,
            text="点击按钮获取今日推荐",
            fg="#333333",
            font=('微软雅黑', 12),
            bg='#F0F8FF'
        )
        self.status.pack(side=tk.BOTTOM, pady=10)

    def on_select_click(self):
        """处理选择按钮点击事件"""
        selected = self.selector.show_selection()
        self.status.config(text=f"已选择: {selected}")

    def start(self):
        """启动应用"""
        self.root.mainloop()