import pygame

class WallUIPrototype :
	
	def __init__(self):
		self.__width 	= 50
		self.__height 	= 50
		# Wall color (190, 183, 159)
		self.__color	= (190, 183, 159)
	
	def draw(self, screen, x, y):
		# print("WallUIPrototype - DRAW")
		pygame.draw.rect(screen, self.__color, (x, y, self.__width, self.__height), 0)
		pygame.draw.rect(screen, (230,223,182), (x, y, self.__width, self.__height), 1)
