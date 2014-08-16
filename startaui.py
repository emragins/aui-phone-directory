import wx
import wx.aui
import info
import textvalidator
import manager
import menufuncts
import editpanel
import listpanel
import shelf


class MainFrame(wx.Frame):
	def __init__(self, parent, title = "Phone Directory.... TWO!"):
		wx.Frame.__init__(self, parent, title = title)
		self.SetMinSize((400,300))
		
		#load any previous data
		self.shelf = shelf.Shelf('default phone directory')
		data = self.shelf.read()
		manager.SetInfo(data)
		
		
		
		panel = wx.Panel(self)
		self.panel = panel
		
		#add panes
		self.listpane = listpanel.ListPanel(panel)
		self.editpane = editpanel.EditPanel(panel)
		
		self.mgr = wx.aui.AuiManager()
		self.mgr.SetManagedWindow(panel)
		
		self.mgr.AddPane(self.listpane, wx.aui.AuiPaneInfo().Left().
						MinSize((140, -1)).Name("list").CloseButton(False))
		self.mgr.AddPane(self.editpane, wx.aui.AuiPaneInfo().Center().MinSize((200,-1)).
						Name("edit").Resizable(True).CloseButton(False))
		self.mgr.Update()
		
		self.AddMenuBar()
		
	def AddMenuBar(self):
		filemenu= wx.Menu()
		entriesmenu=wx.Menu()
		filemenu.Append(wx.ID_OPEN,"&Open","Open a file")
		filemenu.Append(wx.ID_SAVE, "&Save", "Save file over existing file")
		filemenu.Append(wx.ID_SAVEAS, "Save &As...", "Save file")
		filemenu.AppendSeparator()
		filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")
		
		entriesmenu.Append(1, "Sort")
		
		wx.EVT_MENU(self, wx.ID_EXIT, menufuncts.OnExit) 
		wx.EVT_MENU(self, wx.ID_OPEN, menufuncts.OnOpen)
		wx.EVT_MENU(self, wx.ID_SAVE, menufuncts.OnSave)
		wx.EVT_MENU(self, wx.ID_SAVEAS, menufuncts.OnSaveAs)
		wx.EVT_MENU(self, 1, menufuncts.OnSort)
		
		# Creating the menubar.
		menuBar = wx.MenuBar()
		menuBar.Append(filemenu,"&File") # Adding the "filemenu" to the MenuBar
		menuBar.Append(entriesmenu,"&Entries") # Adding the "filemenu" to the MenuBar
		self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.
	
	def EntryAdded(self):
		manager.info.Sort()
		self.UpdateAll()
		self.Save()
		
	def DeleteEntry(self, entry_pos):
		manager.info.DeleteEntry(entry_pos)
		self.UpdateAll()
	
	def Save(self):
		data = manager.GetInfo()
		self.shelf.write(data)
	
	def UpdateAll(self):
		self.listpane.Update()
		entry_pos = self.listpane.GetSelection()
		self.editpane.Update(entry_pos)
		
	def UpdateData(self, entry_pos):
		self.editpane.Update(entry_pos)
	
class MyApp(wx.App):
	def OnInit(self):
		
		self.SetAppName("Phone Directory")
		self.ShowMain()
		return True

	def ShowMain(self):
		frame = MainFrame(None)
		frame.Show()

def main():
	app = MyApp(False)
	app.MainLoop()

	
	
if __name__ == '__main__':
	__name__ = 'Main'
	main()