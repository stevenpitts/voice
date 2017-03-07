#This will be the object that holds the data (which is a sound)
import socket
class Sound:
	def __init__(self,data,user):
		self.data = data
		self.user = user
	def __str__(self):
		return self.user+": \""+self.data+"\""
	def sendData(self,vGUI):
		print "Data has been sent: ",self
		vGUI.sock.send(str(self))
#PyAudio looks good for doing this stuff
class AudioRecorder:
	def __init__(self, gui):
		self.vGUI = gui
	def recordAudio(self):
		#somehow record audio here
		data = "This is what was recorded"
		return data