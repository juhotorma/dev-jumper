import pygame, sys
from random import randint
from ScreenElement import ScreenElement
from BaseModel import BaseModel
from FloorModel import FloorModel
from PlatformModel import PlatformModel
from BaseUIPrototype import BaseUIPrototype
from WallUIPrototype import WallUIPrototype
from SimpleInnerWallUIPrototype import SimpleInnerWallUIPrototype
from SeagulUIPrototype import SeagulUIPrototype
from PlatformUIPrototype import PlatformUIPrototype
from pygame.locals import *

class GameScene:

	# Configurations
	FRAMES_PER_SECOND 	= 30
	MAX_PLATFORMS 		= 5
	
	def __init__ (self, screen) :
		# Engine parts
		self.__screen = screen
		self.__clock = pygame.time.Clock()
		self.__platformEventCounter = 0
							
		# Elements
		self.__elementsOnScreen = []
		self.__SCREEN_ELEMENT_LIMIT = 100
		self.__elementsInScene = 0
		
		self.__SCREEN_ELEMENT_PROTOTYPES = {}
		self.__SCREEN_ELEMENT_PROTOTYPES['base'] = BaseUIPrototype()
		self.__SCREEN_ELEMENT_PROTOTYPES['wall'] = WallUIPrototype()
		self.__SCREEN_ELEMENT_PROTOTYPES['redinnerwall'] = SimpleInnerWallUIPrototype((167,108,78))
		self.__SCREEN_ELEMENT_PROTOTYPES['greeninnerwall'] = SimpleInnerWallUIPrototype((116,57,27))
		self.__SCREEN_ELEMENT_PROTOTYPES['blueinnerwall'] = SimpleInnerWallUIPrototype((193,134,104))
		self.__SCREEN_ELEMENT_PROTOTYPES['seagul'] = SeagulUIPrototype()
		self.__SCREEN_ELEMENT_PROTOTYPES['orangeplatform'] = PlatformUIPrototype((245, 165, 79))
		self.__SCREEN_ELEMENT_PROTOTYPES['turquoiseplatform'] = PlatformUIPrototype((0, 208, 120))
		self.__SCREEN_ELEMENT_PROTOTYPES['greenplatform'] = PlatformUIPrototype((140, 244, 89))
		self.__SCREEN_ELEMENT_PROTOTYPES['redplatform'] = PlatformUIPrototype((203, 56, 56))
		self.__SCREEN_ELEMENT_PROTOTYPES['blueplatform'] = PlatformUIPrototype((156, 186, 180))
		self.__models = {}
		self.__models['bg'] = []
		self.__models['floors'] = []
		self.__models['platforms'] = []

		self.__models['bg'].append(BaseModel(0, 520))
		self.__models['floors'].append(FloorModel(520))
		self.__models['floors'].append(FloorModel(370))
		self.__models['floors'].append(FloorModel(220))
		self.__models['floors'].append(FloorModel(70))
		self.__models['floors'].append(FloorModel(-80))
		self.__models['platforms'].append(PlatformModel('red'))
		self.__models['platforms'].append(PlatformModel('turquoise'))
		self.__models['platforms'].append(PlatformModel('green'))
		self.__models['platforms'].append(PlatformModel('orange'))
		self.__models['platforms'].append(PlatformModel('blue'))
		
		self.__latestPlatform 	= 0
		self.__models['platforms'][0].move(350, 445)
		
		i = 2
		while i < self.MAX_PLATFORMS :
			self.__createPlatform()
			i += 1
		
		i = 0
		while i < self.__SCREEN_ELEMENT_LIMIT:
			self.__elementsOnScreen.append(ScreenElement())
			i += 1
			
		i = 0
		while i < len(self.__models['bg']) :
			self.__models['bg'][i].getElementsToDraw(self)
			i += 1
			
		i = 0
		while i < len(self.__models['floors']) :
			self.__models['floors'][i].getElementsToDraw(self)
			i += 1
			
		i = 0
		while i < len(self.__models['platforms']) :
			self.__models['platforms'][i].getElementsToDraw(self)
			i += 1
			
		i = self.__elementsInScene
		while i < self.__SCREEN_ELEMENT_LIMIT :
			self.__elementsOnScreen[i].clear()
			i += 1
		
	def addScreenElement(self, x, y, prototype):
		if self.__elementsInScene < self.__SCREEN_ELEMENT_LIMIT :
			self.__elementsOnScreen[self.__elementsInScene].assign(x, y, self.__SCREEN_ELEMENT_PROTOTYPES[prototype])
			self.__elementsInScene += 1
		
	
	def __draw(self) :
		print("GAME SCENE - DRAW")
		self.__screen.fill((0,181,215))
					
		if self.__elementsOnScreen is not None and len(self.__elementsOnScreen) > 0 :
			i = 0
			while i < self.__elementsInScene :
				self.__elementsOnScreen[i].draw(self.__screen)
				i += 1

		pygame.display.flip()
		
	def __update(self, speed) :
		if speed <= 0:
			return
		
		print("GAME SCENE - UPDATE")
		self.__elementsInScene = 0
		i = 0
		while i < len(self.__models['bg']) :
			self.__models['bg'][i].update(self,speed)
			i += 1
			
		i = 0
		while i < len(self.__models['floors']) :
			self.__models['floors'][i].update(self,speed)
			i += 1

		i = 0
		while i < len(self.__models['platforms']) :
			self.__models['platforms'][i].update(self,speed)
			i += 1
			
		print("elements after update " + str(self.__elementsInScene))
		
		i = self.__elementsInScene
		while i < self.__SCREEN_ELEMENT_LIMIT :
			self.__elementsOnScreen[i].clear()
			i += 1
			
	def __processTimeEvents (self, speed) :
		self.__platformEventCounter 	+= speed
		
		if speed > 0 and self.__platformEventCounter > 99 :
			print("__processTimeEvents - PLATFORM EVENT")
			self.__createPlatform()
			self.__platformEventCounter = 0
			
	def __createPlatform (self) :
		if self.__latestPlatform < 0 :
			self.__latestPlatform 	= 0
			self.__models['platforms'][0].move(350, 445)
			
		elif self.__latestPlatform == self.MAX_PLATFORMS -1 :
			currentPos 				= self.__models['platforms'][self.__latestPlatform].getPos()
			self.__latestPlatform 	= 0
			
			nextPos 				= self.__calculateNextPos (currentPos)
			self.__models['platforms'][0].move(nextPos['x'], nextPos['y'])
		else :
			currentPos 				= self.__models['platforms'][self.__latestPlatform].getPos()
			self.__latestPlatform 	+= 1
			
			nextPos 				= self.__calculateNextPos (currentPos)
			self.__models['platforms'][self.__latestPlatform].move(nextPos['x'], nextPos['y'])

	def __calculateNextPos(self, pos) :
		limitLeft 		= 350
		limitRight 		= 750
		spaceNeeded 	= 120
		
		posX	 		= pos['x']
		posY	 		= pos['y']
		
		spaceOnLeft 	= posX - limitLeft
		spaceOnRight 	= limitRight - (posX + spaceNeeded)
		side 			= 'left'
	
		if spaceOnLeft > spaceNeeded and spaceOnRight > spaceNeeded :
			rI 			= randint(1,2)
			if rI == 1 :
				side 	= 'left'
			else :
				side 	= 'right'
		elif spaceOnLeft > spaceNeeded :
			side 		= 'left'
		elif spaceOnRight > spaceNeeded :
			side 		= 'right'
			
		distance 		= randint(0,100)
		newPos 			= {}
		newPos['x'] 	= 0
		newPos['y'] 	= 0
		
		if side == 'left' :
				extraSpace 	= spaceOnLeft - spaceNeeded
				deltaX 		= distance if extraSpace > distance else extraSpace
				newPos['x'] = posX - spaceNeeded - deltaX
				newPos['y'] = posY - 100
		elif side == 'right' :
				extraSpace 	= spaceOnRight - spaceNeeded
				deltaX 		= distance if extraSpace > distance else extraSpace
				newPos['x'] = posX + spaceNeeded + deltaX
				newPos['y'] = posY - 100

		return newPos

	def run(self) :
		print("GAME SCENE - RUN")
		speed = 1
		while True :
			deltaT = self.__clock.tick(self.FRAMES_PER_SECOND)
			print("delta since last tick - " + str(deltaT))
			
			for e in pygame.event.get() :
				if hasattr(e, 'key') :
					if e.key == K_ESCAPE :
						sys.exit(0)
			self.__processTimeEvents(speed)
			self.__update(speed)
			self.__draw()
