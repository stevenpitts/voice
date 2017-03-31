import sys
import Tkinter
from Tkinter import *
import socket
import thread
import config
from config import *

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
			#print "1"
			clientSender, clientAddress = self.sock.accept() #blocks other code
			#print "2"
			clientInfoString = clientSender.recv(makuRecVal)
			clientInfo = eval(clientInfoString)
			clientInfo["socket"]=clientSender
			clientInfo["address"]=clientAddress
			self.clients[clientInfo["username"]] = clientInfo
			print "Added client! Info: ",clientInfo
		
	def checkForData(self):
		while (True):
			for client in self.clients.values():
				#print "1"
				sock = client["socket"]
				chunks = []
				counter = 0
				#print "2"
				while True:
					#print "3"
					chunk = sock.recv(makuRecVal)
					if chunk:
						file = open('fisja.wav','wb')
						print "IT GOT SOMETHING"
						while chunk:
							file.write(chunk)
							chunk = sock.recv(makuRecVal)
						file.close()
	def receiveData(self, sound):
		print "Sound has been received: ",sound
if __name__ == '__main__':
	sGUI = SGUI()