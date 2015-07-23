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

	def flushInputs(self):
		curses.flushinp()

	def getStaticKey(self):
		self.screen.nodelay(0)
		K = self.screen.getch()
		self.screen.nodelay(1)
		return K

	def getKey(self):
		"""
			Keys manager.
			Using a thread to wait.
		"""
		t = threading.Thread(target = waiter)
		K = self.screen.getch()
		t.start()
		t.join
		return K

	def printTitleScreen(self):
		"""
			Title screen.
		"""
		curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
		self.screen.addstr( self.H//3 , self.W//3 , "Press SPACE to choose your level difficulty", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 2 , self.W//3 , "or press 'h' for help", curses.color_pair(2))
		self.refreshScreen()

	def printRules(self):
		"""
			Rules screen.
		"""	
		self.clearScreen()
		curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
		self.screen.addstr( self.H//3 , self.W//3 , "*(v)0- Welcome to ASCII-BIRD -0(v)*", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 2, self.W//5 , "Let's talk about the rules", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 4, self.W//5 , "Rule #1: Don't touch the pipes, the ground or the ceilling", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 5, self.W//5 , "Rule #2: Use the spacebar to move your bird", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 6, self.W//5 , "Rule #3: Do the best score ever", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 8, self.W//5 , "Press SPACE to continue", curses.color_pair(2))
		self.refreshScreen()
		
	def printDifficulty(self):
		"""
			Select Difficulty.
		"""	
		self.clearScreen()
		curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
		self.screen.addstr( self.H//3 , self.W//3 , "Choose your destiny", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 2, self.W//5 , "Press a, b ou c to select difficulty", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 4, self.W//5 , "a: Easy. Are you still in your egg?", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 5, self.W//5 , "b: Medium. Nice! You're learning to fly!", curses.color_pair(2))
		self.screen.addstr( self.H//3 + 6, self.W//5 , "c: Hard. You are like an eagle!", curses.color_pair(2))
		self.refreshScreen()
	
	def printScore(self, score):
		"""
			Print live score.
		"""	
		curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
		self.screen.addstr( 1 , 1 , "Your score : " + str(score), curses.color_pair(2))
	
	def printDefeat(self, score):
		"""
			Game Over screen.
		"""
		self.clearScreen()
		curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
		self.screen.addstr( self.H//2 , self.W//3+5 , "GAME OVER!", curses.color_pair(2))
		self.screen.addstr( self.H//2+3 , self.W//3 , "Final score : " + str(score), curses.color_pair(2))
		self.screen.addstr( self.H//2+6 , self.W//3  , "Press Spacebar to restart", curses.color_pair(2))
		self.screen.addstr( self.H//2+7 , self.W//3 , "Press any other key to quit", curses.color_pair(2))
		self.refreshScreen()

	def printBird( self, y , k):
		"""
			Print the bird at the position y with the configuration k.
		"""
		if( y >= self.H):
			self.screen.addstr( self.H-1 , self.posBird , bird[ k ])
			return False
		if( y <= 0):
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
