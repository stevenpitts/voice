import sys
from vGUI import VGUI
import Tkinter
from Tkinter import *

def main(argv=None):
	if argv is None: argv = sys.argv
	root = Tk()
	my_gui = VGUI(root)
	root.mainloop()
	return 0
