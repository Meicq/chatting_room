"""这是客户端主程序"""

from chatting_display import *
from chatting_client import *
from select import *

def main():
    client = Chat_Client(('176.136.4.30',4578))
    tag = client.connect()

    p = epoll()
    fdmap = {client.create_socket().fileno():client.create_socket()}
    p.register(client.create_socket(),EPOLLIN|EPOLLERR|EPOLLOUT)
    events = p.poll()

    
    window = display("python")
    app = window.chat_frame()
    window.chat_frame_title()

    window.frame()
    window.button_send()
    window.button_cancle()
    window.windows()
    window.windows_fixed()
    window.widget_imgInfo()
    window.widget_txtMsg()
    window.widget_txtMsgList()

    def sendMsgEvent(event):
        if event.keysym =='Up':  
            data = window.get_txtMsg()
            print(data)
            window.sendMsg_own()
            client.send_msg(data)
    window.txtMsg.bind("<KeyPress-Up>", sendMsgEvent)
    
    while True:           
        for fd,event_IO in events:
            if event_IO & EPOLLIN:
                data = fdmap[fd].receive_msg()
                window.sendMsg_receive()
        window.chat_frame_update()

    window.chat_frame_mainloop()


main()