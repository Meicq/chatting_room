"""这是服务器功能"""

from socket import *
from multiprocessing import Pipe
import signal
import os, sys

class Chat_Server(object):
    def __init__(self, addr):
        self.server_address = addr
        self.ip = addr[0]
        self.port = addr[1]
        self.create_socket()

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.sockfd.bind(self.server_address)

    def server_forever(self):
        self.sockfd.listen(16)
        print("Listen to the port %d..." % self.port)

        signal.signal(signal.SIGCHLD,signal.SIG_IGN)

        while True:
            connfd, client_address = self.sockfd.accept()
            print("Connect from",client_address)

            # pid = os.fork()
            # parent_pipe, son_pipe = Pipe()
            
            # if pid < 0:
            #     print("进程创建失败!")
            # elif pid == 0:
            #     pass
            # else:
            self.handle_msg(connfd)
    
    def handle_msg(self, connfd):
        # while True:
        data = connfd.recv(1024)
        print(data.decode())

        # msg = input("请输入消息:")
        connfd.send("hello".encode())
        # print("发送成功")
        


addr = ('0.0.0.0',4578)
chatroom = Chat_Server(addr)
chatroom.server_forever()

