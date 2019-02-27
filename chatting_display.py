"""这是封装的图形化界面显示的模块"""

from tkinter import *
import time

class display(object):
    def __init__(self, name):
        self.name = name

    def chat_frame(self):
        self.chatting_frame = Tk()
        return self.chatting_frame

    def chat_frame_title(self):
        self.chatting_frame.title(self.name)
        
    def frame(self):
        #创建frame容器
        self.frmLT = Frame(width = 500, height = 320, bg = 'white')
        self.frmLC = Frame(width = 500, height = 150, bg = 'white')
        self.frmLB = Frame(width = 500, height = 30)
        self.frmRT = Frame(width = 200, height = 500)
    
    def get_txtMsg(self):
        self.msg = self.txtMsg.get('0.0',END)
        return self.msg

    def sendMsg_own(self):
        self.strMsg = "我:" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+ '\n'
        self.txtMsgList.insert(END, self.strMsg, 'greencolor')
        self.txtMsgList.insert(END, self.txtMsg.get('0.0', END))
        self.txtMsg.delete('0.0', END)

    def sendMsg_receive(self,data):
        self.strMsg = "Server:" + time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())+ '\n'
        self.txtMsgList.insert(END, self.strMsg, 'redcolor')
        self.txtMsgList.insert(END, data)
    
    def cancelMsg(self):
        self.txtMsg.delete('0.0', END)

    # def sendMsgEvent(self, event):
    #     if event.keysym =='Up':
    #         self.sendMsg_own()

    def button_send(self):
        self.btnSend = Button(self.frmLB, text = '发送', width = 8, command = self.sendMsg_own)
    
    def button_cancle(self):
        self.btnCancel =Button(self.frmLB, text = '取消', width = 8, command = self.cancelMsg)
    
    def windows(self):
        #窗口布局
        self.frmLT.grid(row = 0, column = 0, columnspan = 2, padx = 1, pady = 3)
        self.frmLC.grid(row = 1, column = 0, columnspan = 2, padx = 1, pady = 3)
        self.frmLB.grid(row = 2, column = 0, columnspan = 2)
        self.frmRT.grid(row = 0, column = 2, rowspan = 3, padx =2, pady = 3)
        self.btnSend.grid(row = 2, column = 0)
        self.btnCancel.grid(row = 2, column = 1)

    def widget_txtMsgList(self):
        #创建控件
        self.txtMsgList = Text(self.frmLT)
        self.txtMsgList.tag_config('greencolor',foreground = '#008C00')#创建tag
        self.txtMsgList.grid()

    def widget_txtMsg(self):
        self.txtMsg = Text(self.frmLC)
        # self.txtMsg.bind("<KeyPress-Up>", self.sendMsgEvent)
        self.txtMsg.grid()

    def widget_imgInfo(self):  
        self.imgInfo = PhotoImage(file = "/home/tarena/中期项目/聊天室/happy.gif")
        self.lblImage = Label(self.frmRT, image = self.imgInfo)
        self.lblImage.image = self.imgInfo
        self.lblImage.grid()       
    
    def windows_fixed(self):
        #固定大小
        self.frmLT.grid_propagate(0)
        self.frmLC.grid_propagate(0)
        self.frmLB.grid_propagate(0)
        self.frmRT.grid_propagate(0)

    def chat_frame_update(self):
        self.chatting_frame.update()

    def chat_frame_mainloop(self):
        self.chatting_frame.mainloop()        
        
    # def main(self):
    #     #创建窗口
    #     app = Tk()
    #     app.title(self.name)

    #     self.frame()
    #     self.button()
    #     self.windows()
    #     self.windows_fixed()
    #     self.widget()

    #     #主事件循环
    #     app.mainloop()

# def main():
#     screen = display("python")
#     app = screen.chat_frame()
#     screen.chat_frame_title()

#     screen.frame()
#     screen.button_send()
#     screen.button_cancle()
#     screen.windows()  
#     screen.windows_fixed()
#     screen.widget_txtMsgList()
#     screen.widget_txtMsg()
#     screen.widget_imgInfo()
#     # print(screen.strMsg)
#     # print(screen.txtMsg)
#     # print(screen.txtMsgList)

#     #主事件循环
#     screen.chat_frame_mainloop()


# main()