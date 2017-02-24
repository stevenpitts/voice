#Steven Pitts
import sys
from vGUI import VGUI
from userSetupGUI import UserSetupGUI
import Tkinter
from Tkinter import *
from sound.sound import Sound

def main(argv=None):
	if argv is None: argv = sys.argv
	infoDict = dict()
	print "infoDict before: ",infoDict
	user_setup_gui = UserSetupGUI(Tk(),infoDict)
	print "infoDictAfter: ",infoDict
	my_gui = VGUI(Tk(),infoDict)
	return 0
