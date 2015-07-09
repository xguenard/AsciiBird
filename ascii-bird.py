import curses 
import time

bird = (  "_o_", "-o-")


class graphics:
	def __init__(self):
		print("Curses initialization")
		self.screen = curses.initscr()
		curses.noecho()
		curses.cbreak()
		self.screen.keypad( True )
		dims = self.screen.getmaxyx()
		self.H = dims[0]
		self.W = dims[1]
		self.bird=0
		self.screen.border()

	def printBird( self, y , k):
		self.screen.clear()
		self.screen.border()
		if(self.bird == 1):
			self.bird = 0
		else :
			self.bird = 1

		self.screen.addstr( y , self.W//8 , bird[ k ])
		self.screen.refresh()


	#def __del__(self):
		#curses.endwin()

############################################

class physics:
	def __init__(self, Ybase ):
		self.G = 10
		self.dir = -1
		self.Y = Ybase

	def calculateY( self, Hmin , Hmax ):
		if( self.Y + self.dir == Hmin + 1 ):
			self.dir = -self.dir
			self.Y = Hmin + 1
		elif(self.Y + self.dir == Hmax -1):
			self.dir = -self.dir
			self.Y = Hmax - 2
		else:
			self.Y += self.dir

	def calculateYError( self, Hmin , Hmax):
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
		self.graphEngine=graphics()
		self.physEngine=physics(self.graphEngine.H//2)

	def start(self):
		for i in range(1,100):
			time.sleep(0.1)
			self.physEngine.calculateY( 0 , self.graphEngine.H )
			self.graphEngine.printBird( self.physEngine.Y , 1 )

#############################################
GameLoop = MainLoop()
GameLoop.start()

