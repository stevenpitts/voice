#This will be the object that holds the data (which is a sound)
import socket
import pyaudio
import wave
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
		self.chunk = 1024
		self.format = pyaudio.paInt16
		self.channels = 2
		self.rate = 44100
		self.recordSeconds = 5
		self.outputFilename = "makuOutput.wav"
		self.p = pyaudio.PyAudio()
		self.vGUI = gui
	def recordAudio(self):
		#somehow record audio here
		stream = self.p.open(format=self.format,channels=self.channels,rate=self.rate,input=True,frames_per_buffer=self.chunk)
		print "recording"
		frames = []
		for i in range(0,int(self.rate/self.chunk*self.recordSeconds)):
			soundData = stream.read(self.chunk)
			frames.append(soundData)
		print "done recording"
		stream.stop_stream()
		stream.close()
		#p.terminate()
		wf=wave.open(self.outputFilename,'wb')
		wf.setnchannels(self.channels)
		wf.setsampwidth(self.p.get_sample_size(self.format))
		wf.setframerate(self.rate)
		wf.writeframes(b''.join(frames))
		#print "thing: ",wf
		wf.close()
		openFile = open(self.outputFilename,'rb')
		return openFile
		#data = "This is what was recorded"
		#return data