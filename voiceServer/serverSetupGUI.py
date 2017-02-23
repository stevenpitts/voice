#Steven Pitts
import Tkinter
from Tkinter import *
class ServerSetupGUI:
	def __init__(self, master, infoDict):
		self.master = master
		master.title("Server Setup")
		
		self.infoDict = infoDict
		
		defaultScreenSize = "500x500"
		master.geometry(defaultScreenSize)
		
		labelText = "Please fill out the information.\n\n"
		self.mainLabel = Label(master, text=labelText)
		self.mainLabel.pack()
		
		self.inputDict = {"ip":Entry(master),
						"port":Entry(master)
						}
		self.labelTextDict = {"ip":"Please enter your ip here",
							"port":"Please enter your port here"
							}
		
		for key in self.inputDict:
			Label(master,text=self.labelTextDict[key]).pack()
			self.inputDict[key].pack()
		
		self.submitButton = Button(master,text="Submit",command=self.pressSubmit)
		self.submitButton.pack()
		
		mainloop()
		
	def pressSubmit(self):
		#check that they've inputted stuff
		for key in self.inputDict:
			self.infoDict[key] = self.inputDict[key].get()
		self.master.destroy()