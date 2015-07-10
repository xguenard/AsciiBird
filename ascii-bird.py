import curses 
import time

bird = (  "_o_", "-o-")


class graphics:
	def __init__(self):
		"""
			Initialization of the window with the curses module.
		"""
		self.screen = curses.initscr()
		curses.noecho()
		curses.cbreak()
		self.screen.keypad( True )
		dims = self.screen.getmaxyx()
		self.H = dims[0]
		self.W = dims[1]
		self.bird=0
		self.screen.border()

	def clearScreen(self):
		"""
			I clear the screen at the beginning of my game loop.
		"""
		self.screen.clear()
		self.screen.border()

	def refreshScreen(self):
		"""
			I refresh the screen at the end of my game loop,
			after filling with printBird and printWall.
		"""
		self.screen.refresh()

	def printBird( self, y , k):
		"""
			Print the bird at the position y with the configuration k.
		"""
		self.screen.addstr( y , self.W//8 , bird[ k ])

	def printWall( self, x , H , side):
		"""
			Print the Wall at the position x, on the side side,with the size H.
		"""
		#side = False => top of the screen, side = True => bottom of the screen
		if( side ):
			self.screen.addstr( H , x , '|__|')
			for i in range( 1 , H ):
				self.screen.addstr(i , x , '|  |')
		else:
			self.screen.addstr(self.H - H , x , ' __ ')
			for i in range( 2 , H ):
				self.screen.addstr( self.H - i , x , '|  |')

	def __del__(self):
		"""
			Destructor.
		"""
		#curses.endwin()

############################################

class physics:
	def __init__(self, Ybase ):
		"""
			Initialize position and gravity.
		"""
		self.G = 10
		self.dir = -1
		self.Y = Ybase

	def calculateY( self, Hmin , Hmax ):
		"""
			My next position depend of the direction.
			This method is for testing.
		"""
		if( self.Y + self.dir == Hmin + 1 ):
			self.dir = -self.dir
			self.Y = Hmin + 1
		elif(self.Y + self.dir == Hmax -1):
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



#############################################

class MainLoop:
	def __init__(self):
		"""
			Initialization of the graphical en physic engine.
		"""
		self.graphEngine=graphics()
		self.physEngine=physics(self.graphEngine.H//2)

	def start(self):
		"""
			Start the game loop.
		"""
		for i in range(1,100):
			self.graphEngine.clearScreen()

			time.sleep(0.1)
			if( i%20 < 10):
				k = 1
			else:
				k = 0
			self.physEngine.calculateY( 0 , self.graphEngine.H )
			self.graphEngine.printBird( self.physEngine.Y , k )
			self.graphEngine.printWall( 15 ,  5 , 0)
			self.graphEngine.printWall( 15 ,  5 , 1)

			self.graphEngine.refreshScreen()

#############################################
GameLoop = MainLoop()
GameLoop.start()

