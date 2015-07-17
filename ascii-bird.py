import time

import graphics
import physics
import walls

#############################################
class TitleScreen:
	def __init__(self, Gengine):
		self.graphEngine= Gengine
		
	def TitleScreen(self):
		#self.graphEngine.printTitleScreen()
		R=-1
		while R!=10:
			R =self.graphEngine.getKey()
			self.graphEngine.printTitleScreen()

class MainLoop:
	def __init__(self, GEngine, PEngine):
		"""
			Initialization of the graphical en physic engine.
		"""
		padding = 30
		vpadding = 10
		self.graphEngine= GEngine
		self.physEngine= PEngine
		self.vpadding = 8
		self.towers = walls.towersManager( GEngine.W , GEngine.H 
									, 30, self.vpadding , GEngine 
									, range(GEngine.posBird-4, GEngine.posBird+6 ))

	def start(self):
		"""
			Start the game loop.
		"""
		cond = True
		i = 0
		while cond:
			R =self.graphEngine.getKey()
			self.graphEngine.clearScreen()

			if (R == 119 or R == 32):
				D = -1
			else:
				D = 0
			self.towers.printTowers()

			time.sleep(0.1)
			if( i%10 < 5):
				k = 1
			else:
				k = 0

			if self.towers.dangerZone:
				cond = self.physEngine.calculateY(D
						, self.towers.dangerZone[0] 
						, self.towers.dangerZone[0] + self.vpadding )
			else:
				cond = self.physEngine.calculateY( D, 0 , self.graphEngine.H )

			if cond:
				cond = self.graphEngine.printBird( self.physEngine.Y , k )
			else:
				tmp = self.graphEngine.printBird( self.physEngine.Y , k )

			self.graphEngine.refreshScreen()

			i+=1

		time.sleep(2)
		self.graphEngine.printDefeat()

#############################################

GraphEngine = graphics.engine()
PhysEngine = physics.engine(GraphEngine.H//2, 5)
GameStart = TitleScreen(GraphEngine)
GameStart.TitleScreen()
GameLoop = MainLoop(GraphEngine, PhysEngine)
GameLoop.start()

