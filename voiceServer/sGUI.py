#Steven Pitts
import Tkinter
from Tkinter import *
import socket
from sound.sound import Sound
import thread
class SGUI:
	def __init__(self, master,infoDict,sock):
	
		#print "1"
		
		self.master = master
		self.port = infoDict["port"]
		self.sock =sock
		self.host = infoDict["host"]
		self.clients = {}
		#self.sock = sock
		master.title("Intercom Server")
		labelText = "The purpose of this is to recieve and echo the messages it recieves.\n\n"
		self.label = Label(master, text = labelText)
		self.label.pack()
		#self.master.after(200,self.checkForData)#Every two seconds, check for new data
		
		thread.start_new_thread(self.checkForClients,())
		thread.start_new_thread(self.checkForData,())
		#print "yes"
		mainloop()
	def checkForClients(self):
		while (True):
			clientSender, clientAddress = self.sock.accept() #I think the code stays on this line until something connects
			clientInfoString = clientSender.recv(1024)
			clientInfo = eval(clientInfoString)
			clientInfo["socket"]=clientSender
			clientInfo["address"]=clientAddress
			self.clients[clientInfo["username"]] = clientInfo
			print "Added client! Info: ",clientInfo
		
	def checkForData(self):
		while (True):
			#print "checking"
			#print "lenclients: ",len(self.clients)
			for client in self.clients.values():
				#print "0"
				sock = client["socket"]
				#socks = [client["socket"] for client in self.clients]
				#for sock in socks:
				#print "1111111111"
				data = sock.recv(1024)
				#print "2222222222"
				#if not data:
					#print "no new data"
				if data:
					self.receiveData(data)
	def receiveData(self, sound):
		print "Sound has been received:"
		print " ",sound