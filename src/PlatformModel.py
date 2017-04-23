class PlatformModel:
	def __init__(self, color):
		self.__posX = 0
		self.__posY = 600
		self.__prototype = color + "platform"
	
	def getElementsToDraw (self, scene):
		scene.addScreenElement(self.__posX, self.__posY, self.__prototype)

	def update (self, scene,speed):
		print("PlatformModel - UPDATE")
		self.__posY += speed
		self.getElementsToDraw(scene)
		
	def move (self, x, y) :
		self.__posX = x
		self.__posY = y
		
	def getPos (self) :
		posStruct 		= {}
		posStruct['x']	= self.__posX
		posStruct['y']	= self.__posY
		
		return posStruct
