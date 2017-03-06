#Steven Pitts
import sys
import socket
from vGUI import VGUI
from userSetupGUI import UserSetupGUI
import Tkinter
from Tkinter import *
from sound.sound import Sound

def main(argv=None):
	if argv is None: argv = sys.argv
	infoDict = dict()
	user_setup_gui = UserSetupGUI(Tk(),infoDict)
	sock = socket.socket()
	infoDict["host"] = socket.gethostname()
	infoDict["port"] = 12345 #should be same on server, I think
	sock.connect((infoDict["host"],infoDict["port"]))
	infoDictString=str(infoDict)
	sock.send(infoDictString)
	
	vGUI = VGUI(Tk(),infoDict,sock)
	
	mainloop()
	return 0
