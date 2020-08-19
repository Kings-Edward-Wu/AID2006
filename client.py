"""
author:凡步
email:???
time:2020-8-13
env:python3.6
socket and Process
"""

from socket import *
from multiprocessing import Process

t_socket = socket(AF_INET,SOCK_DGRAM,proto=0)
addres = ('172.88.8.69',3102)

#创建用户名
while True:
    words = input('新用户名称：\n')
    t_socket.sendto(words.encode(),addres)
    data,addr = t_socket.recvfrom(1024)
    if data.decode() == 'True':
        print('创建用户成功！')
        break
    elif data.decode() == 'False':
        print('创建失败.')
        continue


def get_msg():
    while True:
        data,_ = t_socket.recvfrom(1024)
        print(data.decode())

p = Process(target=get_msg)
p.daemon = True
p.start()

while True:
    words=input('>>>')
    t_socket.sendto(words.encode(),addres)
    if words == 'quit':
        break

t_socket.close()

# while True:
    # words = input('>>>')
    # t_socket.sendto(words.encode(), addres)

