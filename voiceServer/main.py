#Steven Pitts
import sys
import socket
from sGUI import SGUI
from serverSetupGUI import ServerSetupGUI
import Tkinter
from Tkinter import *
from sound.sound import Sound

def main(argv=None):
	if argv is None: argv = sys.argv
	#infoDict = dict()
	#server_setup_gui = ServerSetupGUI(Tk(),infoDict)
	infoDict = {"port":12345,"socket":socket.socket(),"host":socket.gethostname(),"clients":{}}
	
	#sock = socket.socket()
	#host = socket.gethostname()
	#port = int(infoDict["port"])
	infoDict["socket"].bind((infoDict["host"],infoDict["port"]))
	infoDict["socket"].listen(5)
	#clients = {} #Keys should be usernames, values should be infodicts. Append clientSender and clientaddress to infodict.
	sGUI = SGUI(Tk(),infoDict) #How am I going to run the main loop if this is here?
	mainloop()
	return 0
	