import time

import graphics
import physics
import walls

score = 0

class TitleScreen:
	def __init__(self, Gengine):
		self.graphEngine= Gengine
		
	def TitleScreen(self):
		R=-1
		while R!=32 and R!=104:
			R =self.graphEngine.getKey()
			self.graphEngine.printTitleScreen()
		if (R==104):
			while  R!=32:
				R = self.graphEngine.getKey()
				self.graphEngine.printRules()

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
		global score
		score = 0
		scoreBool = False

		self.graphEngine.flushInputs()
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
				scoreBool = True
				cond = self.physEngine.calculateY(D
						, self.towers.dangerZone[0] 
						, self.towers.dangerZone[0] + self.vpadding )
			else:
				cond = self.physEngine.calculateY( D, 0 , self.graphEngine.H )
				if scoreBool:
					score += 1
					scoreBool = False

			if cond:
				cond = self.graphEngine.printBird( self.physEngine.Y , k )
			else:
				tmp = self.graphEngine.printBird( self.physEngine.Y , k )

			self.graphEngine.refreshScreen()

			i+=1

		self.graphEngine.flushInputs()

class EndScreen:
	def __init__(self, Gengine):
		self.graphEngine= Gengine

	def checkForEnd(self):
		time.sleep(1)
		R=-1
		global score
		self.graphEngine.printDefeat(score)
		R =self.graphEngine.getStaticKey()
		if (R==32):
			return True
		return False
		
#############################################
def main():
	GraphEngine = graphics.engine()
	GameStart = TitleScreen(GraphEngine)
	GameStart.TitleScreen()
	GameEnd = EndScreen(GraphEngine)

	cond = True
	while cond:
		PhysEngine = physics.engine(GraphEngine.H//2, 5)
		GameLoop = MainLoop(GraphEngine, PhysEngine)
		GameLoop.start()
		cond = GameEnd.checkForEnd()

if __name__ == "__main__":
	main()