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
	infoDict = dict()
	server_setup_gui = ServerSetupGUI(Tk(),infoDict)
	
	sock = socket.socket()
	host = socket.gethostname()
	port = int(infoDict["port"])
	sock.bind((host,port))
	sock.listen(5)
	clients = {} #Keys should be usernames, values should be infodicts. Append clientSender and clientaddress to infodict.
	sGUI = SGUI(Tk(),infoDict)
	while True: #How am I going to run the main loop if this is here?
		clientSender, clientAddress = sock.accept() #I think the code stays on this line until something connects
		clientIP = clientAddress[0]
		clientSender = clientAddress[1] #I'm not sure what this number is; maybe their port?
		#print sock.recv(1024) #what's this do?
		clientStuff.send("AYYIT WORKD")
		#sock.close #Maybe don't do this
	mainloop()
	return 0
	