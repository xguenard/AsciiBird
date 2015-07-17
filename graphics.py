import curses
import threading
import time
bird = ( "*(v)0-", "*(^)0-")
tow =  ( "|__|" , "|  |" , " __ " )

def waiter():
	time.sleep(0.1)

class engine:
	def __init__(self):
		"""
			Initialization of the window with the curses module.
		"""
		self.screen = curses.initscr()
		curses.noecho()
		self.screen.keypad( True )
		self.screen.nodelay(1)
		dims = self.screen.getmaxyx()
		self.H = dims[0]
		self.W = dims[1]
		self.posBird=self.W//8
		self.screen.border()
		curses.start_color()

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

	def getKey(self):
		"""
			Keys manager.
			Using a thread to wait.
		"""
		t = threading.Thread(target = waiter)
		K = self.screen.getch()
		#FOR DEBUGGING
		#self.screen.addstr(2 , 2 , "DEBUG INFO :" + str(K)) 
		#self.screen.refresh()
		t.start()
		t.join
		return K

	def printTitleScreen(self):
		"""
			Title screen.
		"""
		curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
		self.screen.addstr( self.H//3 , self.W//3 , "Press the Spacebar to start", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 2 , self.W//3 , "or press 'h' for help", curses.color_pair(2))
		self.refreshScreen()

	def printRules(self):
		"""
			Rules screen.
		"""	
		self.clearScreen()
		curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
		self.screen.addstr( self.H//3 , self.W//3 , "Test rules", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 2, self.W//3 , "Press SPACE to cotinue", curses.color_pair(2))
		self.refreshScreen()
		
	def printDefeat(self):
		"""
			Game Over screen.
		"""
		self.clearScreen()
		self.screen.addstr( self.H//2 , self.W//2 , "GAME OVER!")
		self.refreshScreen()

	def printBird( self, y , k):
		"""
			Print the bird at the position y with the configuration k.
		"""
		if( y == self.H):
			self.screen.addstr( y-1 , self.posBird , bird[ k ])
			return False
		if( y == 0):
			self.screen.addstr( 0 , self.posBird , bird[ k ])
			return False
		self.screen.addstr( y , self.posBird , bird[ k ])
		return True

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

