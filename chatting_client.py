"""这是封装的客户端连接模块"""

from socket import *
from tkinter import * 
import os,sys
import time

class Chat_Client(object):
    def __init__(self, addr):
        self.server_address = addr
        self.create_socket()

    def create_socket(self):
        self.sockfd = socket()
        return self.sockfd

    def connect(self):
        try:
            self.sockfd.connect(self.server_address)
        except Exception as e:
            print(e)

    def send_msg(self, data):
        print("这是send_msg里面的data:",data)
        while True:
            if not data:
                break
            self.sockfd.send(data.encode())
            # print("发送成功")

    def receive_msg(self):
        self.msg = self.sockfd.recv(1024).decode()
        return self.msg

    
    

