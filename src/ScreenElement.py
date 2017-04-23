class ScreenElement :
	__posX = 0
	__posY = 0
	__prototype = None
	
	def draw (self, screen) :
		self.__prototype.draw(screen, self.__posX, self.__posY)
		
	def assign (self, x, y, elementPrototype) :
		self.__posX = x
		self.__posY = y
		self.__prototype = elementPrototype
		
	def clear (self) :
		self.__posX = 0
		self.__posY = 0
		self.__prototype = None
		
	
