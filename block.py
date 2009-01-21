import pygame, random

class Block(pygame.sprite.Sprite):

	def __init__(self, color, pos, size):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface(size)
		self.image.fill(color)

		self.rect = self.image.get_rect()
		self.rect.center = pos

	def roam(self):
		xpos, ypos = 0, 0
		direction1 = random.randint(0,1)
		direction2 = random.randint(-5,5)
		if direction1 == 0:
			xpos += direction2
		elif direction1 == 1:
			ypos += direction2

		self.rect.move_ip(xpos, ypos)

	def update(self):
		self.roam()
