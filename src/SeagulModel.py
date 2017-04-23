from random import randint

class SeagulModel:	
	def __init__(self, x, y):
		self.__posX 			= x
		self.__posY 			= y
		self.__prototype 		= "seagul"
		self.__speedHorizontal 	= randint(1,4)
	
	def getElementsToDraw (self, scene):
		scene.addScreenElement(self.__posX, self.__posY, self.__prototype)

	def update (self, scene, speed):
		print("SeagulModel - UPDATE") 
		self.__posY += speed
		self.__posX += self.__speedHorizontal
		self.getElementsToDraw(scene)
