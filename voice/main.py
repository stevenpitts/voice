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
	vGUI = VGUI(Tk(),infoDict)
	
	sock = socket.socket()
	host = socket.gethostname()
	port = 12345 #should be same on server, I think
	sock.connect((host,port))
	print sock.recv(1024)
	sock.close
	
	mainloop()
	return 0
