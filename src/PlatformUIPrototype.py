import pygame

class PlatformUIPrototype :
	
	def __init__(self, color):
		self.__width 	= 100
		self.__height 	= 30
		self.__color 	= color	
	
	def draw(self, screen, x, y):
		pygame.draw.rect(screen, self.__color, (x, y, self.__width, self.__height), 0)
		pygame.draw.rect(screen, (0,0,0), (x, y, self.__width, self.__height), 1)
