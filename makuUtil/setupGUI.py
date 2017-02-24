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
		#check that they've inputted stuff
		for key in self.inputDict:
			self.infoDict[key] = self.inputDict[key].get()
		self.master.destroy()
	def populate(self):
		for key in self.inputDict:
			self.inputDict[key].insert(0,key+"Default")