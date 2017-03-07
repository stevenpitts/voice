#Steven Pitts
import Tkinter
from Tkinter import *
#from makuUtil.setupGUI import SetupGUI
import setupGUI
from setupGUI import SetupGUI
class UserSetupGUI:
	def __init__(self, master, infoDict):
		self.master = master
		self.infoDict = infoDict
		
		self.inputDict = {"username": Entry(master),
			"firstName":Entry(master),
			"lastName":Entry(master)
			}
		self.labelTextDict = {"username":"Please enter your username here",
			"firstName":"Please enter your first name here",
			"lastName":"Please enter your last name here"
			}
		user_setup_gui = SetupGUI(self.master,self.infoDict,self.inputDict,self.labelTextDict)