#Steven Pitts
import sys
from sGUI import SGUI
from serverSetupGUI import ServerSetupGUI
import Tkinter
from Tkinter import *
from sound.sound import Sound

def main(argv=None):
	if argv is None: argv = sys.argv
	infoDict = dict()
	print "infoDict before: ",infoDict
	server_setup_gui = ServerSetupGUI(Tk(),infoDict)
	print "infoDict after: ",infoDict
	my_gui = SGUI(Tk(),infoDict)
	return 0
