"""
非阻塞 IO
"""
from socket import *
import time

# 创建tcp套接字
sock = socket()
sock.bind(("0.0.0.0", 2727))
sock.listen(5) # sock监听套接字

# 设置套接字为非阻塞
sock.setblocking(False)

# 设置超时检测
sock.settimeout(3)

# 接受客户端连接
while True:
    try:
        print("waiting for connect...")
        connfd, addr = sock.accept()
        print("Connect from",addr)
    except BlockingIOError as e:
        time.sleep(2)
        # a 以追加模式打开,若文件不存在则新建
        with open("test.log","a") as f:
            msg = "%s : %s\n" % (time.ctime(),e)
            f.write(msg)
    except timeout as e:
        with open("test.log","a") as f:
            msg = "%s : %s\n" % (time.ctime(),e)
            f.write(msg)
    else:
        # 与链接有关的事情
        data = connfd.recv(1024).decode()
        print(data)
