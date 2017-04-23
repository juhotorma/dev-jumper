import pygame

class BaseUIPrototype :
	__width = 800
	__height = 75
	
	def draw(self, screen, x, y):
		print("BaseUIPrototype - DRAW")
		pygame.draw.rect(screen, (0,0,0), (x, y, self.__width, self.__height), 0)
