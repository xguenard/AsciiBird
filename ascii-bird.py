import time

import graphics
import physics
import walls
import event

#############################################

class MainLoop:
	def __init__(self, GEngine, PEngine):
		"""
			Initialization of the graphical en physic engine.
		"""
		padding = 30
		vpadding = 10
		self.graphEngine= GEngine
		self.physEngine= PEngine
		self.towers = walls.towersManager( GEngine.W , GEngine.H 
									, 30, 5 , GEngine 
									, range(GEngine.posBird-4, GEngine.posBird+6 ))

	def start(self):
		"""
			Start the game loop.
		"""
		for i in range(1,100):
			self.graphEngine.clearScreen()
			self.towers.printTowers()

			time.sleep(0.1)
			if( i%20 < 10):
				k = 1
			else:
				k = 0

			if self.towers.dangerZone:
				print("test")
				self.physEngine.calculateY( self.towers.dangerZone[0] , self.towers.dangerZone[0] + 5 )
			else:
				self.physEngine.calculateY( 0 , self.graphEngine.H )

			self.graphEngine.printBird( self.physEngine.Y , k )

			self.graphEngine.refreshScreen()

#############################################

GraphEngine = graphics.engine()
keyHandler = event.keysManager(GraphEngine)
PhysEngine = physics.engine(GraphEngine.H//2, keyHandler)
GameLoop = MainLoop(GraphEngine, PhysEngine)
GameLoop.start()

