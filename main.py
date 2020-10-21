import pygame
import sys


pygame.init()

#Variables.
player_cords = [0, 0]
grid_unit = 20



#Creating the three main surfaces.
room_resolution = [800, 800]
camera_resolution = [800, 800]
window_resolution = [800, 800]


camera = pygame.Surface(camera_resolution)
window = pygame.display.set_mode(window_resolution)



#Creating snake head class.
class player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		global player_cords
		self.image = pygame.Surface((20, 20))
		self.image.fill((0, 255, 0))
		self.rect = self.image.get_rect()
		self.rect.topleft = player_cords
	def logic(self):
		player_cords[0] += 1
		self.rect.topleft = player_cords


#Creating player sprite and group
player_spr = pygame.sprite.Group()
playr = player()
player_spr.add(playr)


#Quit the game function definition.
def quit():
	pygame.quit()
	sys.exit()

#Creating object for tracking time
clock = pygame.time.Clock()

while True:

	delta = clock.tick(60)
	camera.fill((0, 0, 0))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			quit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				quit()
#Player logic
	playr.logic()


#Drawing sprites to screen
	player_spr.draw(camera)


	window.blit(pygame.transform.scale(camera, (window_resolution)), (0, 0))

#Updating the screen
	pygame.display.update()
