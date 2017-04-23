class BaseModel:

	def __init__(self, x, y):
		self.__posX = x
		self.__posY = y
		self.__prototype = "base"
	
	def getElementsToDraw (self, scene):
		scene.addScreenElement(self.__posX, self.__posY, self.__prototype)

	def update (self, scene,speed):
		print("BaseModel - UPDATE") 
		self.__posY += speed
		self.getElementsToDraw(scene)
