from random import randint
from SeagulModel import SeagulModel
from WallModel import WallModel
from SimpleInnerWallModel import SimpleInnerWallModel

class FloorModel:	
	def __init__(self, currentHeight):
		self.__posX = 0
		self.__posY = currentHeight - 150
		self.__build()
		
	def __build (self) :
		self.__children = []
		self.__children.append(SimpleInnerWallModel(300, self.__posY))
		self.__children.append(WallModel(300, self.__posY))
		self.__children.append(WallModel(750, self.__posY))
		self.__children.append(WallModel(300, self.__posY + 50))
		self.__children.append(WallModel(750, self.__posY + 50))
		self.__children.append(WallModel(300, self.__posY + 100))
		self.__children.append(WallModel(750, self.__posY + 100))
		
		i = randint(1,10)
		if i > 1 and i < 4 :
			self.__children.append(SeagulModel(0, self.__posY + 25))

	def getElementsToDraw (self, scene):		
		for c in self.__children :
			c.getElementsToDraw(scene)

	def update (self, scene,speed):
		print("FloorModel - UPDATE, children " + str(len(self.__children)) + " " + str(self.__posY))
		self.__posY += speed
		
		if self.__posY < 600 :
			for c in self.__children :
				c.update(scene,speed)
		else :
			self.__posY -= 750
			
			while len(self.__children) > 0 :
				c = self.__children.pop()
				del c
			
			self.__build()
			
			for c in self.__children :
				c.getElementsToDraw(scene)
