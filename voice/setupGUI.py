#Steven Pitts
import Tkinter
from Tkinter import *
class SetupGUI:
	def __init__(self, master, infoDict):
		self.master = master
		master.title("Setup")
		
		self.infoDict = infoDict
		
		defaultScreenSize = "500x500"
		master.geometry(defaultScreenSize)
		
		labelText = "Please fill out the information."
		self.label = Label(master, text=labelText)
		self.label.pack()
		
		self.nameEntry = Entry(master)
		self.nameEntry.pack()
		self.nameEntry.insert(0,"Please insert your name here")
		
		#There will be more in the future
		
		self.submitButton = Button(master,text="Submit",command=self.pressSubmit)
		self.submitButton.pack()
		
		mainloop()
		
	def pressSubmit(self):
		#check that they've inputted stuff
		self.infoDict["name"] = self.nameEntry.get()
		self.master.destroy()