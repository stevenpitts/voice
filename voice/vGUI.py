#Steven Pitts
import Tkinter
from Tkinter import *
from sound.sound import Sound
from sound.audioRecorder import AudioRecorder
import sys
import socket
from userSetupGUI import UserSetupGUI

class VGUI:
	def __init__(self):
		
		
		infoDict = {}
		user_setup_gui = UserSetupGUI(Tk(),infoDict)
		self.sock = socket.socket()
		self.host = socket.gethostname()
		self.port = 12345
		self.firstName = infoDict["firstName"]
		self.lastName = infoDict["lastName"]
		self.sock.connect((self.host,self.port))
		
		infoDict["host"] = self.host
		infoDict["port"] = self.port
		infoDictString = str(infoDict)
		self.sock.send(infoDictString)
		
		self.master = Tk()
		
		"""#infoDict = dict()
		#user_setup_gui = UserSetupGUI(Tk(),infoDict)
		sock = socket.socket()
		infoDict["host"] = socket.gethostname()
		infoDict["port"] = 12345 #should be same on server, I think
		sock.connect((infoDict["host"],infoDict["port"]))
		infoDictString=str(infoDict)
		sock.send(infoDictString)"""
		
		#vGUI = VGUI(Tk(),infoDict,self.sock)
		
		
		
		
		#self.master = master
		#self.sock = sock
		self.audioRecorder = AudioRecorder(self)
		#self.host = infoDict["host"]
		#self.port = infoDict["port"]
		#self.firstName = infoDict["firstName"]
		#self.lastName = infoDict["lastName"]
		
		self.master.title("Intercom")
		
		Label(self.master, text = "Send your message to others on the network!\n\n").pack()
		self.record_button = Button(self.master, text="Record Message",command=self.recordPress)
		self.record_button.pack()
		mainloop()
		
	
	def recordPress(self):
		wasRecording = (self.record_button["text"] == "Stop Recording") #There must be a better way of doing this
		if wasRecording:
			data = self.audioRecorder.recordAudio()
			self.sendData(data)
			self.record_button["text"] = "Record Message"
		else:
			self.record_button["text"] = "Stop Recording"
	def sendData(self, data):
		newSound = Sound(data,self.getName())
		newSound.sendData(self)
	def getName (self):
		return self.firstName+" "+self.lastName