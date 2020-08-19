from socket import *
from threading import Thread
import os, time

HOST = "0.0.0.0"
PORT = 2727
ADDR = (HOST, PORT)

FTP = "/home/tarena/FTP/"

class FTPServer(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super(FTPServer, self).__init__()

    # 获取文件列表
    def view(self):
        file_list = os.listdir(FTP)

        if not file_list:
            self.connfd.send(b"FALSE")
            return
        else:
            self.connfd.send(b"OK")
            time.sleep(0.1)  # 防止粘包
            file = "\n".join(file_list)
            self.connfd.send(file.encode())

    def download(self):
        data = self.connfd.recv(1024)
        print(data.decode())

    # 处理来自客户端的信息,总分模型部分
    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if data == "VIEW":
                self.view()
            elif data == "download":
                self.download()
            else:
                break

def main():
    sock = socket()
    sock.bind(ADDR)
    sock.listen(5)

    print("等待客户端端口 %d 连接..." % PORT)
    while True:
        connfd, addr = sock.accept()
        print("Connect from ", addr)

        t = FTPServer(connfd)
        t.start()

if __name__ == '__main__':
    main()




























    # def get_list(connfd):
    #     file_list = os.listdir(FTP)
    #     files = "\n".join(file_list)
    #     while True:
    #         data = connfd.recv(1024)
    #         if data == "get list".encode():
    #             connfd.send(files.encode())
    #         elif data == "download".encode():
    #             file = open("/home/tarena/FTP/data02.txt","rb")
    #
    #             msg = file.read(1024*1024)
    #             if  not msg:
    #                 break
    #             connfd.send(msg)
    #
    #
    #         else:
    #             connfd.send("FALSE".encode())
