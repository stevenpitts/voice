import sys
import Tkinter
from Tkinter import *
import socket
import thread
import config
from config import *
import time

#from voiceServer import SGUI

class SGUI:
	def __init__(self):
		
		self.master = Tk()
		self.port = makuPort
		self.sock =socket.socket()
		self.host = socket.gethostname()
		self.sock.bind((self.host,self.port))
		self.sock.listen(makuMaxClients)
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
			clientInfoString = clientSender.recv(makuRecVal)
			clientInfo = eval(clientInfoString)
			clientInfo["socket"]=clientSender
			clientInfo["address"]=clientAddress
			self.clients[clientInfo["username"]] = clientInfo
			print "Added client! Info: ",clientInfo
		
	def checkForData(self):
		while (True):
			for client in self.clients.values():
				sock = client["socket"]
				sock.setblocking(0)
				chunks = []
				counter = 0
				while True:
					chunk = 0
					#GOTTA DO NON-BLOCKING STUFF HERE
					try:
						chunk = sock.recv(makuRecVal)
					except socket.error, (value,message):
						chunk = 0
					if chunk:
						file = open('receivedFile.wav','wb')
						while chunk:
							file.write(chunk)
							try:
								chunk = sock.recv(makuRecVal)
							except socket.error, (value,message):
								chunk = 0
						file.close()
						file2 = open('receivedFile.wav','rb')
						for client2 in self.clients.values():
							client2["socket"].sendall(file2.read())
						
	def receiveData(self, sound):
		print "Sound has been received: ",sound
if __name__ == '__main__':
	sGUI = SGUI()