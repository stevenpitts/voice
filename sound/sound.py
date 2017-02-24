#This will be the object that holds the data (which is a sound)
class Sound:
	def __init__(self,data,user):
		self.data = data
		self.user = user
	def sendData(self):
		print "The user ",self.user," has send the data: ",self.data