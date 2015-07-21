
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

	def calculateYTest( self, Hmin , Hmax ):
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

	def calculateY(self, V , Hmin , Hmax):
		"""
			Where is my bird at the next time step?
		"""
		self.calculateDir()
		if V!= 0 :
			if self.dir > 0 :
				self.dir = -1
			elif self.dir > -2:
				self.dir -= 1
		return self.calculateYError( Hmin , Hmax)

	def calculateDir(self):
		"""
			An approximation of gravity's speed modification ... with integers.
		"""
		if (self.dir != 2) :
			if( self.rest > 0.5 ):
				self.dir += 1
				self.rest = 0
			else:
				self.rest += self.G/self.timePadding

	def calculateYError( self, Hmin , Hmax):
		"""
			My next position depends of the direction.
			I also check collisions.
		"""
		if( self.Y  <= Hmin   ):
			return False
		elif(self.Y >= Hmax ):
			return False
		else:
			self.Y += self.dir
			return True

