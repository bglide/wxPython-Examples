import wx

class myFrame(wx.Frame):
    def __init__(self, parent, title):
        super(myFrame, self).__init__(parent, title=title,
            size=(350, 250))

def main():
    app = wx.App(clearSigInt=True)
    ex = myFrame(None, title='This is my frame!')
    ex.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()