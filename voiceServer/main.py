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
	server_setup_gui = ServerSetupGUI(Tk(),infoDict)
	sGUI = SGUI(Tk(),infoDict)
	return 0
