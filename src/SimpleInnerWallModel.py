from random import randint

class SimpleInnerWallModel:
	
	def __init__(self, x, y):
		self.__posX = x
		self.__posY = y
		
		i = randint(1,3)
		color = "red"
		if i == 1 :
			color = "red"
		elif i == 2 :
			color = "green"
		elif i == 3 :
			color = "blue"
		
		self.__prototype = color + "innerwall"
	
	def getElementsToDraw (self, scene):
		scene.addScreenElement(self.__posX, self.__posY, self.__prototype)

	def update (self, scene,speed):
		print("SimpleInnerWallModel - UPDATE") 
		self.__posY += speed
		self.getElementsToDraw(scene)
