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
			print "1"
			clientSender, clientAddress = self.sock.accept() #blocks other code
			print "2"
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
				chunks = []
				while True:
					chunk = sock.recv(makuRecVal)
					if not chunk: break
					print "323322"
					chunks.append(chunk)
				if chunks:
					print "chunks: ",chunks
					recFile = wave.open('rec.wav','rb')
					recFile.write(b''.join(chunks))
					recFile.close()
					self.receiveData(chunks)
	def receiveData(self, sound):
		print "Sound has been received: ",sound
if __name__ == '__main__':
	sGUI = SGUI()