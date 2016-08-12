"""
 Pygame base template for opening a window

 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/

 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import random
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (129, 129, 129)
colors = [BLACK, GREEN, BLUE, RED]

#from PIL import Image



def random_color():
	return random.choice(colors)
# initialize the pygame class
pygame.init()

# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
#screen.blit ("moon.jpg", (0,0) )


#Set the title of the window
pygame.display.set_caption("CityScroller")


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

total = 0
building_list = []

class Building():
	
	def __init__(self, x_point, y_point, width, height, color):
		self.x_point = x_point
		self.y_point = y_point
		self.width = width
		self.height = -height
		self.color = color

	def draw(self):
	
		pygame.draw.rect(screen, self.color, (self.x_point, self.y_point, self.width, self.height))
		
	def move(self, speed):
		
		self.x_point -= speed


class Scroller(object):
	

	def __init__(self, width, height, base, color, speed):
		self.width = width
		self.height = height
		self.base = base
		self.color = color
		self.speed = speed
	
	def add_buildings(self):
		
		takes in an x_location, an integer, that represents where along the x-axis to
		put a buildng.
		Adds a building to list of buildings.
	
		This calls the draw method on each building.
	
	
		for i in building_list:
			i.move(self.speed)
		

FRONT_SCROLLER_COLOR = GREEN
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
#(0,0,30)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 100, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)

front_scroller.add_buildings()
middle_scroller.add_buildings()
back_scroller.add_buildings()

# -------- Main Program Loop -----------
while not done:
	# --- Main event loop
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True

	
	
	screen.fill(BACKGROUND_COLOR)



	back_scroller.draw_buildings()
	back_scroller.move_buildings()
	middle_scroller.draw_buildings()
	middle_scroller.move_buildings()
	front_scroller.draw_buildings()
	front_scroller.move_buildings()
	
	
	pygame.display.flip()

	# --- Limit to 60 frames per second
	clock.tick(30)
# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLEs