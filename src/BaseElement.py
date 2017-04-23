import pygame

class BaseElement :
	__cX = 0
	__cY = 0
	__width = 800
	__height = 75
	
	def __init__ (self, x, y):
		self.__cX = x
		self.__cY = y
	
	def draw(self, screen):
		print("BaseElement - DRAW")
		pygame.draw.rect(screen, (0,0,0), (self.__cX, self.__cY, self.__width, self.__height), 0)

	def clone(self, x, y) :
		return BaseElement(x, y)
