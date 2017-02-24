#This will be the object that holds the data (which is a sound)
class Sound:
	def __init__(self,data,user):
		self.data = data
		self.user = user
	def __str__(self):
		return self.user+": \""+self.data+"\""
	def sendData(self):
		print "Data has been sent:"
		print " ",self