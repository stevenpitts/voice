#Steven Pitts
import Tkinter
from Tkinter import *
class SetupGUI:
	def __init__(self, master, infoDict, inputDict, labelTextDict):
		self.master = master
		master.title("Setup")
		
		self.infoDict = infoDict
		
		defaultScreenSize = "500x500"
		master.geometry(defaultScreenSize)
		
		labelText = "Please fill out the information.\n\n"
		self.mainLabel = Label(master, text=labelText)
		self.mainLabel.pack()
		self.inputDict = inputDict
		self.labelTextDict = labelTextDict
		for key in self.inputDict:
			Label(master,text=self.labelTextDict[key]).pack()
			self.inputDict[key].pack()
		self.submitButton = Button(master,text="Submit",command=self.pressSubmit)
		self.submitButton.pack()
		
		self.populateButton = Button(master, text="Autopopulate (for debugging)",command=self.populate)
		self.populateButton.pack()
		
		mainloop()
		
	def pressSubmit(self):
		for key in self.inputDict:
			entryVal = self.inputDict[key].get()
			if (entryVal == ""):
				self.mainLabel["text"] = "One or more spaces are blank. Please fill out the form."
				return
			self.infoDict[key] = entryVal
		self.master.destroy()
	def populate(self):
		for key in self.inputDict:
			self.inputDict[key].insert(0,key+"Default")
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