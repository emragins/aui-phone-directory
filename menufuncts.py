'''
THESE WILL NOT WORK RIGHT
	
EXIT, however, works.
'''
import wx
import manager

def OnOpen(e):
	parent = e.GetEventObject()
	value = None
	dlg = wx.FileDialog(parent, "Choose a file", parent.dirname, "", "*.*", wx.OPEN)
	if dlg.ShowModal() == wx.ID_OK:
		filename=dlg.GetFilename()
		dirname=dlg.GetDirectory()
		value = parent.shelf.read(filename)
	parent.filename = filename
	parent.dirname = dirname
	dlg.Destroy()
	return value

def OnSave(e):
	parent = e.GetEventObject()
	parent.Save()

def OnSaveAs(e):
	parent = e.GetEventObject()
	dlg = wx.FileDialog(parent, "Save as...", parent.dirname, "", "*.*", wx.SAVE)
	if dlg.ShowModal() == wx.ID_OK:
		parent.filename=dlg.GetFilename()
		parent.dirname=dlg.GetDirectory()
		parent.shelf.ChangeFiles(parent.filename)
		parent.shelf.write(parent.info)
	dlg.Destroy()

def OnExit(e):
	OnSave(e)
	parent = e.GetEventObject()
	parent.Close(True)  # Close the frame.
	
#------------
def OnSort(e):
	parent = e.GetEventObject()
	print 'lo'
	info = manager.GetInfo()
	info.Sort()
	manager.SetInfo(info)
	parent.UpdateAll()