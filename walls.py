import math
import random

class tower:
	def __init__(self , maxW , maxH, padding , vpadding):
		self.X = maxW - 5 #I start on the right of the screen
		sqrPad = int( math.sqrt(2)*(padding-1) )
		if( maxH <= sqrPad):
			R = random.randint( 2 , int(maxH - 2 - vpadding) ) #random height
		else:
			R = random.randint(int(maxH//2 - sqrPad//2) , int( maxH//2 + sqrPad//2 -2 - vpadding) )
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
	def __init__(self, maxW, maxH, padding , vpadding, Gengine, birdPos):
		self.towerList = []
		self.maxW = maxW
		self.maxH = maxH
		self.maxElem = maxW//padding +1
		self.minDist = maxW - padding - 6
		self.padding = padding
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
			self.towerList.append( tower( self.maxW , self.maxH, self.padding, self.vpadding ) )

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
