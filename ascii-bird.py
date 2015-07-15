import time
import random
import graphics
import physics
############################################

class tower:
	def __init__(self , maxW , maxH):
		self.X = maxW - 5 #I start on the right of the screen
		R = random.randint( 2 , int(maxH - 10) ) #random height
		self.H = R

	def update(self,birdPos, dangerZone):
		if( self.X == 2 ):
			return False
		else :
			self.X -= 1
			if( self.X in birdPos ):
				dangerZone.append(self.H)
		return True


###########################################
class towersManager:
	def __init__(self, maxW, maxH, padding, vpadding, Gengine, birdPos):
		self.towerList = []
		self.maxW = maxW
		self.maxH = maxH
		self.maxElem = maxW//padding
		self.minDist = maxW - padding
		self.graphEngine = Gengine
		self.vpadding = vpadding
		self.dangerZone = []
		self.birdPos = birdPos


	def checkLastTower(self):
		if not self.towerList :
			return True
		if self.towerList[-1].X < self.minDist:
			return True
		return False

	def addTower(self):
		if( len(self.towerList) <= self.maxElem and self.checkLastTower() ):
			self.towerList.append( tower( self.maxW , self.maxH ) )

	def moveTowers(self):
		self.dangerZone = []
		for Twr in self.towerList:
			if not Twr.update(self.birdPos, self.dangerZone):
				self.towerList.remove(Twr)

	def printTowers(self):
		self.moveTowers()
		self.addTower()
		for Twr in self.towerList:
			self.graphEngine.printWall(Twr.X , Twr.H , 1)
			self.graphEngine.printWall(Twr.X , self.maxH - Twr.H - self.vpadding , 0)


#############################################

class MainLoop:
	def __init__(self, GEngine, PEngine):
		"""
			Initialization of the graphical en physic engine.
		"""
		self.graphEngine= GEngine
		self.physEngine= PEngine
		self.towers = towersManager(80 , 25 , 20, 5 ,GEngine, range(GEngine.posBird-1, GEngine.posBird+6 ))

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
PhysEngine = physics.engine(GraphEngine.H//2)
GameLoop = MainLoop(GraphEngine, PhysEngine)
GameLoop.start()

