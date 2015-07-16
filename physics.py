class engine:
	def __init__(self, Ybase , tPadding):
		"""
			Initialize position and gravity.
		"""
		self.G = 1
		self.dir = 0
		self.Y = Ybase
		self.timePadding = tPadding
		self.rest = 0

	def calculateY( self, Hmin , Hmax ):
		"""
			My next position depend of the direction.
			This method is for testing.
		"""

		if( self.Y + self.dir < Hmin + 1 ):
			self.dir = -self.dir
			self.Y = Hmin + 1
		elif(self.Y + self.dir > Hmax -1):
			self.dir = -self.dir
			self.Y = Hmax - 2
		else:
			self.Y += self.dir

	def calculateY2(self, V , Hmin , Hmax):
		self.calculateDir()
		if V != 0:
			self.dir = V
		self.calculateY( Hmin , Hmax)


	def calculateDir(self):
		if (self.dir != 1) :
			if( self.rest > 0.5 ):
				self.dir += 1
				self.rest = 0
			else:
				self.rest += self.G/self.timePadding


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

