import pygame, random

class Player(pygame.sprite.Sprite):

	def __init__(self, color, pos, size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(size)
		self.image.fill(color)

		self.rect = self.image.get_rect()
		self.rect.center = pos

	def roam(self, keypress):
		xpos, ypos = 0, 0

		# Convert keypress to a coordinate shift for player sprite
		if keypress == pygame.K_LEFT:
			xpos = -5
		elif keypress == pygame.K_RIGHT:
			xpos = 5
		elif keypress == pygame.K_UP:
			ypos = -5
		elif keypress == pygame.K_DOWN:
			ypos = 5

		self.rect.move_ip(xpos, ypos)

	def update(self, keypress):
		self.roam(keypress)
