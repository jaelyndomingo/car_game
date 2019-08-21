import pygame
import time
import random
import gameFuncs

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
off_white = (244,243,233)
light_green = (181,213,96)
yellow = (244,207,94)
orange = (242,172,29)

car_width = 80

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

carImg = pygame.image.load('car.png')


def things_dodged(count):
	font = pygame.font.SysFont(None, 25)
	text = font.render("Dodged: " + str(count), True, black)
	gameDisplay.blit(text, (0,0))


def things(thingx, thingy, thingw, thingh, color):
	pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])


def car(x,y):
	gameDisplay.blit(carImg, (x,y))


def message_display(text):
	large_text = pygame.font.Font('freesansbold.ttf', 115)
	TextSurf, TextRect = gameFuncs.text_objects(text, large_text)
	TextRect.center = ((display_width/2), (display_height/2))
	gameDisplay.blit(TextSurf, TextRect)

	pygame.display.update()
	time.sleep(2)


def crash():
	message_display('You Crashed!')
	print('crashed')
	game_loop()


def game_intro():
	intro = True

	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

		background_image = pygame.image.load('start_menu.png').convert()
		background_image = pygame.transform.scale(background_image, (800,600))
		gameDisplay.blit(background_image, (0,0))

		gameFuncs.button(gameDisplay, "LET'S GO!", 150, 450, 150, 50, off_white, light_green)
		gameFuncs.button(gameDisplay, "Quit", 500, 450, 150, 50, orange, yellow)

		pygame.display.update()
		clock.tick(15)


def game_loop():
	x = (display_width * 0.45)
	y = (display_height * 0.8)
	x_change = 0
	car_speed = 7

	thing_startx = random.randrange(0, display_width - 100)
	thing_starty = -600
	thing_speed = 7
	thing_width = 100
	thing_height = 100
	thing_count = 0

	game_exit = False

	while not game_exit:								# game loop

		for event in pygame.event.get():
			if event.type == pygame.QUIT:			# user exits out of window
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:		# if key pressed
				if event.key == pygame.K_LEFT:		# move left
					x_change = -car_speed
				if event.key == pygame.K_RIGHT:		# move right
					x_change = car_speed

			if event.type == pygame.KEYUP:			# if key released
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0

		x += x_change								# update x value

		gameDisplay.fill(white)

		things(thing_startx, thing_starty, thing_width, thing_height, black)
		thing_starty += thing_speed
		car(x,y)
		things_dodged(thing_count)

		if x > display_width - car_width or x < 0:	# if car goes out of bounds
			crash()									# crash message displayed

		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0, display_width)
			thing_count += 1
			thing_speed += 1
			thing_width += (thing_count * 1.2)
			print(thing_count)


		if y < (thing_starty + thing_height):		# car hits bottom left

			if (x > thing_startx and x < (thing_startx + thing_width)) or ((x + car_width) > thing_startx and (x + car_width) < (thing_startx + thing_width)):
													# car is anywhere in rectangle's boundaries
				crash()

		pygame.display.update()
		clock.tick(60) 								# 60 FPS


game_intro()
game_loop()
pygame.quit()
quit()