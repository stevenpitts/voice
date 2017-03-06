#Steven Pitts
import Tkinter
from Tkinter import *
from sound.sound import Sound
class SGUI:
	def __init__(self, master,infoDict):
	
		#print "1"
		
		self.master = master
		#self.infoDict = infoDict
		self.port = infoDict["port"]
		self.sock = infoDict["socket"]
		self.host = infoDict["host"]
		self.clients = {}
		
		master.title("Intercom Server")
		labelText = "The purpose of this is to recieve and echo the messages it recieves.\n\n"
		self.label = Label(master, text = labelText)
		self.label.pack()
		self.addClientButton = Button(master,text="Add Client",command=self.addClient)
		self.addClientButton.pack()
		#demoSound = Sound("This is the demo data","Steven Demo")
		#self.receiveData(demoSound)
		#print demoSound
	def receiveData(self, sound):
		print "Sound has been received:"
		print " ",sound
	def addClient(self):
		clientSender, clientAddress = self.sock.accept() #I think the code stays on this line until something connects
		#clientIP = clientAddress[0]
		#clientSender = clientAddress[1] #I'm not sure what this number is; maybe their port?
		clientInfoString = clientSender.recv(1024) #what's this do?
		clientInfo = eval(clientInfoString)
		clientInfo["socket"]=clientSender
		clientInfo["address"]=clientAddress
		print "Added client! Info: ",clientInfo
		
		#print "Client lastname: ",clientInfo["lastName"]
		#clientStuff.send("AYYIT WORKD")
		#sock.close #Maybe don't do this
