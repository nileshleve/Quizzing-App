import wx


class secondClass(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(secondClass, self).__init__(*args, **kwargs)

        self.basicGUI()

    def basicGUI(self):

        panel = wx.Panel(self,size=(300,300))


        menuBar = wx.MenuBar()

        fileButton = wx.Menu()

        aweText = wx.StaticText(panel, wx.ID_ANY, "Awesome Text", pos=(145,40))
        
        buttonConnect = wx.Button(panel, id=wx.ID_ANY, label='Connect', pos=(140,10))
        buttonConnect.Bind(wx.EVT_BUTTON, self.Connect_me)

                
        buttonSubmit = wx.Button(panel, id=wx.ID_ANY, label='Submit', pos=(90,100))
        buttonSubmit.Bind(wx.EVT_BUTTON, self.Submit)

        buttonNext = wx.Button(panel, id=wx.ID_ANY, label='Next', pos=(190,100))
        buttonNext.Bind(wx.EVT_BUTTON, self.Next_song)
        
        wx.TextCtrl(panel, pos=(130,70))
        
        exitItem = fileButton.Append(wx.ID_EXIT, 'Exit','status msg...')

        menuBar.Append(fileButton, 'File')

        self.SetMenuBar(menuBar)
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        self.SetTitle('Welcome ')
        self.Show(True)

    def Next_song(self, e):
        self.SetTitle("Next")
        print "next"

    def Submit(self, e):
        self.SetTitle("Submitted")
        print "submitted"

    def Quit(self, e):
        self.Close()

    def Connect_me(self, e):
        self.SetTitle("Connected")
        print "connected"



def main():
    app = wx.App()
    secondClass(None)

    app.MainLoop()

main()
    
