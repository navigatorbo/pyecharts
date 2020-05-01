#wxPython

# import wx
# app=wx.App()  #创建一个应用程序对象
# frame = wx.Frame(None,title = "Hello World!") #创建一个Frame框架对象，frame是其他UI组件的容器
# frame.Show(True) #显示窗体
# app.MainLoop() #进入事件循环，只能够读事件找函数调用，必须写，否则程序没响应

# #以面向对象的方式实现
# import wx
# class MyApp(wx.App):   #从wx派生子类
# 	#OnInit()方法在应用程序开始时并且在MainLoop开始之前就被wxPython系统调用
# 	def OnInit(self):  #定义一个应用程序的初始化方法
# 		frame = wx.Frame(None,title= 'hello world!')
# 		frame.Show()
# 		return True
# if __name__=='__main__':
# 	app=MyApp()
# 	app.MainLoop()

# import wx
# class Frame1(wx.Frame):
#     def __init__(self,superior):
#         wx.Frame.__init__(self,parent = superior,title = "Example",pos = (100,200),size = (350,200))
#         panel = wx.Panel(self)
#         text1 = wx.TextCtrl(panel, value="Hello world", size=(350, 200))
# if __name__ == '__main__':
#     app = wx.App()
#     frame =Frame1(None)
#     frame.Show(True)
#     app.MainLoop()

# #派生Frame子类,将字符串显示到窗体当中去
# import wx
# class Framel(wx.Frame):
# 	def __init__(self,superior):
# 		wx.Frame.__init__(self,parent = superior,title="Example",pos=(100,200),size=(350,200))
# 		self.panel= wx.Panel(self)
# 		self.panel.Bind(wx.EVT_LEFT_UP,self.OnClick) # 将鼠标左键抬起时间，绑在panel的OnClick()方法上
# 	def OnClick(self,event):
# 		posm = event.GetPosition()
# 		wx.StaticText(parent=self.panel,label = "hello world!",pos =(posm.x,posm.y))
# if __name__=='__main__':
# 	app = wx.App()
# 	frame = Framel(None)
# 	frame.Show(True)
# 	app.MainLoop()

import wx
class Frame1(wx.Frame):
    def __init__(self,superior):
        wx.Frame.__init__(self,parent=superior,title="hello World in wxPython")
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        self.text1 = wx.TextCtrl(panel,value="Hello,world!",size=(200,180),style=wx.TE_MULTILINE)
        sizer.Add(self.text1,0,wx.ALIGN_TOP|wx.EXPAND)
        button = wx.Button(panel,label = "Click Me")
        sizer.Add(button)
        panel.SetSizerAndFit(sizer)
        panel.Layout()
        self.Bind(wx.EVT_BUTTON,self.OnClick,button)
    def OnClick(self,text):
        self.text1.AppendText("\nHello,world!")
if __name__ == '__main__':
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()