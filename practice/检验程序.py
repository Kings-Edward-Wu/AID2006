# # 根据列表中的数字,重复生成*.
# #     list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# #     效果：
# #         *
# #         **
# #         ***
# #         ****
# #         *****
# #         ****
# #         ***
# #         **
# #         *
# # list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
# # for item in list01:
# #     print("*" * item)
#
# """
#     2. 将列表中的数字累乘
#         list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
#     结果：806400
# """
# # list02 = [5, 1, 4, 6, 7, 4, 6, 8, 5]
# # result = 1
# # for item in list02:
# #     result *= item
# # print(result)
#
# """
#     3. 将列表中整数的个位不是5和3的数字存入另外一个列表
#         list03 = [25, 63, 27, 75, 70, 83, 27]
#     结果:[27, 70, 27]
# """
# # list03 = [25, 63, 27, 75, 70, 83, 27]
# # list04 = []
# # for item in list03:
# #     if item % 10 == 5 or item % 10 == 3:
# #         continue
# #     list04.append(item)
# # print(list04)
#
# list01 = ["a",["b", "c"]]
# # 浅拷贝，只备份一层数据(两份)
# # 第二层数据只有一份
# # list02 = list01[:]
# # print(list02)
# # list01[0] = "A" # 修改第一层
# # list01[1][0] = "B" # 修改第二层
# # print(list02)  # ['a', ['B', 'c']]
#
# # data01 = ["a", "b", "c"]
# # data01[0] = "A"
# # data01[1:] = ["B", "C"]  # 将右侧列表元素赋值给左侧
# # print(data01)
# # data02 = ["a", "b", "c"]
# # data02[0] = ["B", "C"]  # 将右侧列表地址赋值给左侧
# # data02[1:] = "DE"
# # print(data02)  # [['B', 'C'], 'D', 'E']
#
# # 计算给定字符串列表中字符串⻓度⼤于2，并且第⼀个和最后⼀个字符相同的字符串个数
# #     字符串列表：words =["qtx","看一看","想啊想","练练"]
# #     结果:2
# # words =["qtx","看一看","想啊想","练练"]
# # count = 0
# # for item in words:
# #     if len(item) > 2 and item[0] == item[-1]:
# #         count += 1
# # print(count)
#
# # 在终端中录入疫情地区名称，如果输入空字符串，则停止。
# #    最后倒序打印所有地区名称(一行一个)
# #    要求：录入的名称已经存在不要再次添加.
# #    提示： in
#
# list_place = []
# while True:
#     place = input("请输入地区名称：")
#     if place == "":
#         break
#     if place in list_place:
#         print("已经存在")
#     else:
#         list_place.append(place)
# print(list_place)
#
# for i in range(len(list_place) - 1 , -1, -1):
#     print(list_place[i])

# def display_message(what):
#     print("本章将要学习" + what)
#
# display_message("函数")
#
# def favorite_book(title):
#     print("One of my favorite books is " + str(title))
#
# favorite_book("Alice in Wonderland")


# 小A和小B在玩猜数字.小B每次从1,2,3中随机选择一个,小A每次也从1,2,3中选择一个猜。他们一共进行三次这个游戏，请返回小A猜对了几次？
# 输入的guess数组为小A每次的猜测，answer数组为小B每次的选择.guess和answer的长度都等于3

# import random
#
# guess = []
# answer = []
# number = 0
#
# for i in range(3):
#     guess_random = random.randint(1, 3)
#     answer_random = random.randint(1, 3)
#     guess.append(guess_random)
#     answer.append(answer_random)
#
#     if guess[i] == answer[i]:
#             number += 1
# print(guess)
# print(answer)
# print("小A一共猜对了%d次"% number)
#
# class Dogs:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(self.name + " is now sitting")


