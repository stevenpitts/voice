#Steven Pitts
import Tkinter
from Tkinter import *
from sound.sound import Sound
"""
Resources:
http://python-textbok.readthedocs.io/en/1.0/Introduction_to_GUI_Programming.html'
https://docs.python.org/2/library/tkinter.html
"""
class SGUI:
	def __init__(self, master,infoDict):
	
		
		
		self.master = master
		self.infoDict = infoDict
		
		master.title("Intercom Server")
		
		labelText = "The purpose of this is to recieve and echo the messages it recieves.\n\n"
		self.label = Label(master, text = labelText)
		self.label.pack()
		demoSound = Sound("This is the demo data","Steven Demo")
		self.receiveData(demoSound)
		print demoSound
		mainloop()
	def receiveData(self, sound):
		print "Sound has been received:"
		print " ",sound