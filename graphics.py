import curses

bird = ( "*(v)0-", "*(^)0-")
tow =  ( "|__|" , "|  |" , " __ " )

class engine:
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
		self.posBird=self.W//8
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
		self.screen.addstr( y , self.posBird , bird[ k ])

	def printWall( self, x , H , side):
		"""
			Print the Wall at the position x, on the side side,with the size H.
		"""
		#side = False => top of the screen, side = True => bottom of the screen
		if( side ):
			self.screen.addstr( H , x , tow[0])
			for i in range( 1 , H ):
				self.screen.addstr(i , x , tow[1])
		else:
			self.screen.addstr(self.H - H , x , tow[2])
			for i in range( 2 , H ):
				self.screen.addstr( self.H - i , x , tow[1])

	def __del__(self):
		"""
			Destructor.
		"""
		curses.endwin()

