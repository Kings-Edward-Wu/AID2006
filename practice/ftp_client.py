from socket import *

ADDR = ("127.0.0.1", 2727)


class FTPClient(object):
    def __init__(self, sock):
        self.sock = sock

    def view(self):
        # 发送请求
        self.sock.send(b"VIEW")
        # 等待反馈
        result = self.sock.recv(128)
        if result == b"OK":
            # 接收文件列表
            file = self.sock.recv(1024)
            print(file.decode())
        else:
            print("文件库为空")

    def download(self):
        file_name = input("请输入要下载文件名称:")
        self.sock.send(file_name.encode())


def main():
    sock = socket()
    sock.connect(ADDR)

    ftp = FTPClient(sock)

    while True:
        msg = input(">>>")
        if msg == "VIEW":
            ftp.view()
        elif msg == "download":
            ftp.download()


if __name__ == '__main__':
    main()