import wx

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        # create a panel to put our button on
        self.panel = wx.Panel(self)
        
        # create the button
        self.but = wx.Button(self.panel,label="Press Me!",pos=(100,100))
        
        # define what the button will do
        def onclick1(self):
            textframe = wx.Frame(None,size=(350, 250))
            text = wx.StaticText(textframe,label="I am Groot")
            textframe.Show()
        
        self.but.Bind(wx.EVT_BUTTON,onclick1)
        
def main():

    app = wx.App()
    ex = Example(None,title="Frame with Menu")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()