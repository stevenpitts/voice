#Steven Pitts
import Tkinter
from Tkinter import *
"""
Resources:
http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html'
https://docs.python.org/2/library/tkinter.html
"""
class VGUI:
	def __init__(self, master):
		self.master = master
		master.title("Intercom")
		
		labelText = "The purpose of this is for recording messages to be sent to other computers on the network."
		self.label = Label(master, text = labelText)
		self.label.pack()
		
		self.record_button = Button(master, text="Record Message",command=self.recordPress)
		#self.record_button["WasRecording"] = 0 This didn't work
		self.record_button.pack()
		
		self.close_button = Button(master, text="Close Window",command=master.quit)
		self.close_button.pack()
	
	def recordPress(self):
		wasRecording = (self.record_button["text"] == "Stop Recording") #There must be a better way of doing this
		if wasRecording:
			print "Normally, this would stop the recording."
			self.record_button["text"] = "Record Message"
		else:
			print "Normally, this would start a recording."
			self.record_button["text"] = "Stop Recording"