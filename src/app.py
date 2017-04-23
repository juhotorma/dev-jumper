import pygame
from pygame.locals import *
from GameScene import GameScene

class App :
	def run(self):
		print("DEV-JUMPER")
		pygame.init()
		screen = pygame.display.set_mode((800, 600), DOUBLEBUF)
		scene = GameScene(screen)
		scene.run()


def main():
	app = App()
	app.run()

main()
