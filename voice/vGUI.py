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
		master.title("The title")
		
		self.label = Label(master, text = "Label text")
		self.label.pack()
		
		self.greet_button = Button(master, text="Greet button text",command=self.greet)
		self.greet_button.pack()
		
		self.close_button = Button(master, text="Close",command=master.quit)
		self.close_button.pack()
	
	def greet(self):
		print "Howdy!"

root = Tk()
my_gui = VGUI(root)
root.mainloop()