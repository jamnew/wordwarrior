import sys, pygame, random, block, player

pygame.init()
pygame.key.set_repeat(1, 1)
size = width, height = 800, 600
screen = pygame.display.set_mode(size)

count = 0

blockGroup = pygame.sprite.RenderUpdates()
playerGroup = pygame.sprite.RenderUpdates()

# Create block or blocks
while count < int(sys.argv[1]):
	obj = block.Block([random.randint(0,255),random.randint(0,255),random.randint(0,255)], [random.randint(0,width),random.randint(0,height)], [10,10])
	blockGroup.add(obj)
	count += 1

# Create player
obj = player.Player([255,0,0], [400,500], [20,20])
playerGroup.add(obj)

while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # Window close event
			sys.exit()
		elif event.type == pygame.KEYDOWN: # Key pushed event
			if event.key == pygame.K_ESCAPE:
				sys.exit()
			elif event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				playerGroup.update(event.key)

	# Draw all the sprites in the block group to the screen.
	blockGroup.clear(screen, pygame.Surface(size))
	reclist = blockGroup.draw(screen)
	pygame.display.update(reclist)
	blockGroup.update()

	# Draw all the sprites in the player group to the screen.
	playerGroup.clear(screen, pygame.Surface(size))
	reclist = playerGroup.draw(screen)
	pygame.display.update(reclist)
