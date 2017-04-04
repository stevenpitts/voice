import sys
import Tkinter
from Tkinter import *
import sys
import socket
from config import *
import pyaudio
import wave
import config
import time
from config import *
from shutil import copyfile
import thread

class SetupGUI:
	def __init__(self, master, infoDict, inputDict, labelTextDict):
		self.master = master
		master.title("Setup")
		
		self.shouldStopRecording = False
		
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
		
		
class VGUI:
	def __init__(self):
		
		
		infoDict = {}
		user_setup_gui = UserSetupGUI(Tk(),infoDict)
		self.sock = socket.socket()
		hostname,aliaslist,ipaddress = socket.gethostbyaddr(makuServerIP) #Should be host IP
		self.host = hostname
		self.port = makuPort
		self.firstName = infoDict["firstName"]
		self.lastName = infoDict["lastName"]
		self.sock.connect((self.host,self.port))
		infoDict["host"] = self.host
		infoDict["port"] = self.port
		infoDictString = str(infoDict)
		self.sock.send(infoDictString)
		self.master = Tk()
		#self.audioRecorder = AudioRecorder(self)
		
		self.p = pyaudio.PyAudio()
		
		self.master.title("Intercom")
		Label(self.master, text = "Send your message to others on the network!\n\n").pack()
		self.record_button = Button(self.master, text="Record Message",command=self.recordPress)
		self.record_button.pack()
		print "b4thread"
		thread.start_new_thread(self.contCheckForAudio,())
		print "aftrthrea"
		mainloop()
		
	
	def recordPress(self):
		#wasRecording = (self.record_button["text"] == "Stop Recording") #There must be a better way of doing this
		if wasRecording:
			print "was"
			#data = self.recordAudio()
			#self.shouldStopRecording = True
			#self.record_button["text"] = "Record Message"
		else:
			data = self.recordAudio()
			self.sock.sendall(data.read())
			#self.record_button["text"] = "Stop Recording"
	def sendData(self, data):
		self.sock.send(data.read())
	def getName (self):
		return self.firstName+" "+self.lastName
	def recordAudio(self):
		stream = self.p.open(format=makuFormat,channels=makuChannels,rate=makuRate,input=True,frames_per_buffer=makuChunk)
		print "recording"
		frames = []
		for i in range(0,int((makuRate/makuChunk)*makuRecordSeconds)):
			soundData = stream.read(makuChunk)
			frames.append(soundData)
		print "done recording"
		stream.stop_stream()
		stream.close()
		wf=wave.open(makuOutputFilename,'wb')
		wf.setnchannels(makuChannels)
		wf.setsampwidth(self.p.get_sample_size(makuFormat))
		wf.setframerate(makuRate)
		wf.writeframes(b''.join(frames))
		wf.close()
		openFile = open(makuOutputFilename,'rb')
		return openFile
	def contCheckForAudio(self):
		print "einseofns"
		self.sock.setblocking(0)
		while (True):
			chunk = 0
			try:
				chunk = self.sock.recv(makuRecVal)
			except socket.error, (value,message):
				chunk = 0
			if chunk:
				file = open(makuClientInputFilename,"wb")
				while chunk:
					file.write(chunk)
					try:
						chunk = self.sock.recv(makuRecVal)
					except socket.error, (value,message):
						chunk = 0
				file.close()
				self.playAudio()
	def playAudio(self):
		chunk = makuChunk
		file = wave.open(makuClientInputFilename,"rb")
		p = pyaudio.PyAudio()
		stream = p.open(format=p.get_format_from_width(file.getsampwidth()),channels=file.getnchannels(),rate=file.getframerate(),output=True)
		data = file.readframes(chunk)
		while data:
			stream.write(data)
			data = file.readframes(chunk)
		stream.stop_stream()
		stream.close()
		p.terminate
		
if __name__ == '__main__':
	vGUI = VGUI()
	mainloop()