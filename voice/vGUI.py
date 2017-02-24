#Steven Pitts
import Tkinter
from Tkinter import *
"""
Resources:
http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html'
https://docs.python.org/2/library/tkinter.html
"""
class VGUI:
	def __init__(self, master,infoDict):
	
		
		
		self.master = master
		self.infoDict = infoDict
		
		master.title("Intercom")
		
		labelText = "The purpose of this is for recording messages to be sent to other computers on the network."
		self.label = Label(master, text = labelText)
		self.label.pack()
		self.record_button = Button(master, text="Record Message",command=self.recordPress)
		self.record_button.pack()
		
		self.recDataEntry = Entry(master)
		
		mainloop()
	
	def recordPress(self):
		wasRecording = (self.record_button["text"] == "Stop Recording") #There must be a better way of doing this
		if wasRecording:
			print "Normally, this would stop the recording."
			self.sendData(self.recDataEntry.get())#This will send what's in the rec data box thing
			self.recDataEntry.pack_forget()
			self.record_button["text"] = "Record Message"
		else:
			print "Normally, this would start a recording."
			self.recDataEntry.pack()
			self.recDataEntry.delete(0,END)
			self.record_button["text"] = "Stop Recording"
	def sendData(self, data):
		print "The user ",self.getName()," has send the data: ",data
		#This should actually send it in the future
	def getName (self):
		return self.infoDict["firstName"]+" "+self.infoDict["lastName"]