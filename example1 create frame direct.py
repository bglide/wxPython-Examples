import wx

app = wx.App(clearSigInt=True)
myframe = wx.Frame(None,title='This is my frame!',size=(350, 250))
myframe.Show()
app.MainLoop()