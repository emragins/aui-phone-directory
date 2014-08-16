import time
import info
import wx

info = info.Info()

def GetInfo():
	global info 
	return info

def SetInfo(data):
	global info
	info = data
	
def wait(ms):
	mytime = time.clock()
	while time.clock() < mytime + ms*0.0001:
		print time.clock()
		print mytime + ms
	return
