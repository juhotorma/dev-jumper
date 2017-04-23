import pygame

class SeagulUIPrototype :
	
	def __init__(self):
		self.__width = 120
		self.__height = 100		
	
	def draw(self, screen, x, y):
		# print("SeagulUIPrototype - DRAW")
		pygame.draw.rect(screen, (127,127,127), (x, y, self.__width, self.__height), 0)
		pygame.draw.rect(screen, (0,0,0), (x, y, self.__width, self.__height), 1)
