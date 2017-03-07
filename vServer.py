import sys
import Tkinter
from Tkinter import *
import socket
import thread

#from voiceServer import SGUI

class SGUI:
	def __init__(self):
		
		self.master = Tk()
		self.port = 12345
		self.sock =socket.socket()
		self.host = socket.gethostname()
		self.sock.bind((self.host,self.port))
		self.sock.listen(5)
		self.clients = {}
		self.master.title("Intercom Server")
		labelText = "The purpose of this is to recieve and echo the messages it recieves.\n\n"
		self.label = Label(self.master, text = labelText)
		self.label.pack()
		
		thread.start_new_thread(self.checkForClients,())
		thread.start_new_thread(self.checkForData,())
		mainloop()
		
	def checkForClients(self):
		while (True):
			clientSender, clientAddress = self.sock.accept() #blocks other code
			clientInfoString = clientSender.recv(1024)
			clientInfo = eval(clientInfoString)
			clientInfo["socket"]=clientSender
			clientInfo["address"]=clientAddress
			self.clients[clientInfo["username"]] = clientInfo
			print "Added client! Info: ",clientInfo
		
	def checkForData(self):
		while (True):
			for client in self.clients.values():
				sock = client["socket"]
				data = sock.recv(1024)
				if data:
					self.receiveData(data)
	def receiveData(self, sound):
		print "Sound has been received: ",sound
if __name__ == '__main__':
	sGUI = SGUI()