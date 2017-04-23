class WallModel:	
	def __init__(self, x, y):
		self.__posX = x
		self.__posY = y
		self.__prototype = "wall"
	
	def getElementsToDraw (self, scene):
		scene.addScreenElement(self.__posX, self.__posY, self.__prototype)

	def update (self, scene, speed):
		# print("WallModel - UPDATE") 
		self.__posY += speed
		self.getElementsToDraw(scene)
