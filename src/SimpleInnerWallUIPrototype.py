import pygame

class SimpleInnerWallUIPrototype :
	
	def __init__(self, color):
		self.__width = 500
		self.__height = 150
		self.__color = color
	
	def draw(self, screen, x, y):
		# print("SimpleInnerWallUIPrototype - DRAW")
		pygame.draw.rect(screen, self.__color, (x, y, self.__width, self.__height), 0)
		pygame.draw.rect(screen, (92, 67, 61), (x, y  + 140 , self.__width, self.__height - 140), 0)
