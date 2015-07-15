import time
import random
import graphics
import physics
############################################

class tower:
	def __init__(self , maxW , maxH):
		self.X = maxW - 5 #I start on the right of the screen
		slef.H = random.randrang( 2 , maxH - 6) #random height


class towersManger:
	def __init__(self, maxW):
		self.towerList = []
		self.maxElem = maxW//15

#############################################

class MainLoop:
	def __init__(self, GEngine, PEngine):
		"""
			Initialization of the graphical en physic engine.
		"""
		self.graphEngine= GEngine
		self.physEngine= PEngine

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
			self.graphEngine.printWall( 18 ,  5 , 0)
			self.graphEngine.printWall( 18 ,  15 , 1)

			self.graphEngine.refreshScreen()

#############################################

GraphEngine = graphics.engine()
PhysEngine = physics.engine(GraphEngine.H//2)
GameLoop = MainLoop(GraphEngine, PhysEngine)
GameLoop.start()

