#Steven Pitts
import Tkinter
from Tkinter import *
from makuUtil.setupGUI import SetupGUI
class ServerSetupGUI:
	def __init__(self, master, infoDict):
		self.master = master
		self.infoDict = infoDict
		
		
		self.inputDict = {"ip":Entry(master),
						"port":Entry(master)
						}
		self.labelTextDict = {"ip":"Please enter your ip here",
							"port":"Please enter your port here"
							}
		server_setup_gui = SetupGUI(self.master,self.infoDict,self.inputDict,self.labelTextDict)