#Steven Pitts
import sys
#from vGUI import VGUI
from serverSetupGUI import ServerSetupGUI
import Tkinter
from Tkinter import *

def main(argv=None):
	if argv is None: argv = sys.argv
	infoDict = dict()
	print "infoDict before: ",infoDict
	server_setup_gui = ServerSetupGUI(Tk(),infoDict)
	print "infoDict after: ",infoDict
	return 0
