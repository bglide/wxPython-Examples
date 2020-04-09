import wx

class Example(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Example, self).__init__(*args, **kwargs)

        self.InitUI()

    def InitUI(self):
        # add a bar to the frame to which I can add menus
        menubar = wx.MenuBar() 
        
         # create the individual menus
        fileMenu = wx.Menu()
        fileMenu2 = wx.Menu()
        
        # add stuff to each menu
        fileitem0 = fileMenu2.Append(wx.ID_EXIT, 'General Kenobi')
        fileItem = fileMenu.Append(wx.ID_EXIT, 'Hello there')
        
        # add the menus to the menu bar
        menubar.Append(fileMenu, '&Hey look at me first!')
        menubar.Append(fileMenu2, '&Then look at me!')
        self.SetMenuBar(menubar)
        
def main():

    app = wx.App()
    ex = Example(None,title="Frame with Menu")
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()