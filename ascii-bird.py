import curses 
import time

bird = ( "/\\", "\\/" )


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

	def printBird( self, y):
		self.screen.clear()
		if(self.bird == 1):
			self.bird = 0
		else :
			self.bird = 1

		self.screen.addstr( self.H//2 - y, self.W//8 , bird[ self.bird ])
		self.screen.refresh()


	def __del__(self):
		curses.endwin()

############################################

class physics:
	def __init__(self):
		self.G = 10

#############################################

class MainLoop:
	def __init__(self):
		self.buffer=graphics()
		self.engine=physics()

	def start(self):
		for i in range(1,10):
			time.sleep(1)
			k = i%2 - 1
			self.buffer.printBird( k )

#############################################
GameLoop = MainLoop()
GameLoop.start()

