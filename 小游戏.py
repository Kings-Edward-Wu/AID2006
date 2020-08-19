
# from random import randint
#
# def play():
#     random_int = randint(0,100)
#
#     while True:
#         user_guess = int(input("what number did we guess (0-100)?"))
#
#         if user_guess == random_int:
#             print(f"You found the number {random_int}.Congrats!")
#             break
#
#         if user_guess < random_int:
#             print("Your number is less than number we guessed.")
#             continue
#
#         if user_guess >random_int:
#             print("Your number is more than the number we guessed.")
#             continue
#
# if __name__ == '__main__':
#     play()

# from random import randint
#
# computer = randint(0,100)
# you = int(input("请输入你猜的数字："))
# if computer == you:
#     print("恭喜您猜对了！")
# elif you > computer:
#     print("您猜大了")
# else:
#     print("您猜小了！")


"""
PyAutoGUI——做职场高手,让所有GUI自动化,击败无聊的办公室重复性操作
GUI:图形用户界面(Graphical User Interface)
例如 办公软件,音乐播放器,即时通讯工具...
盘点工作中的机械化重复性操作：

作用：自动控制鼠标和键盘。
文档：https://pyautogui.readthedocs.io/en/latest/install.html
安装：
1. 打开运行窗口 win + r
2. 输入cmd，进入命令行。
3. 输入pip install pyautogui
"""
# 准备一个自动化工具
import pyautogui

# 显示鼠标位置
# pyautogui.displayMousePosition()

# 使用自动化工具的移动功能
# pyautogui.moveTo(x轴坐标,y轴坐标,持续时间)
pyautogui.moveTo(37, 735, 3) # 移动到酷狗

# # 使用自动化工具的双击功能
pyautogui.doubleClick() # 打开酷狗

# 等待
pyautogui.sleep(5)
pyautogui.displayMousePosition()
# 1. 截图
# pyautogui.screenshot("play.png", region=(485, 621, 50, 50))

# 2. 定位
button7location = pyautogui.locateOnScreen("play.png")
play_button_point = pyautogui.center(button7location)

# 移动到播放按钮
pyautogui.moveTo(play_button_point.x, play_button_point.y, 3)
pyautogui.click() # 单击

