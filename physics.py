class engine:
	def __init__(self, Ybase , event):
		"""
			Initialize position and gravity.
		"""
		self.G = 10
		self.dir = -1
		self.Y = Ybase
		self.eventHandler = event
		self.eventHandler.launchThread()


	def getDir(self):
		if self.eventHandler.stack :
			self.eventHandler.stack.pop(0)
			self.dir = -1
		else:
			self.dir = 1

	def calculateY( self, Hmin , Hmax ):
		"""
			My next position depend of the direction.
			This method is for testing.
		"""
		self.getDir()

		if( self.Y + self.dir < Hmin + 1 ):
			self.dir = -self.dir
			self.Y = Hmin + 1
		elif(self.Y + self.dir > Hmax -1):
			self.dir = -self.dir
			self.Y = Hmax - 2
		else:
			self.Y += self.dir

	def calculateYError( self, Hmin , Hmax):
		"""
			My next position depend of the direction.
		"""
		if( self.Y + self.dir == Hmin + 1 ):
			return False
		elif(self.Y + self.dir == Hmax -1):
			return False
		else:
			self.Y += self.dir
			return True

