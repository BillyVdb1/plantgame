from re import X
from subprocess import Popen
from tkinter import Y
from turtle import left
import pygame
import Score 



# initializing the constructor
pygame.init()

# screen resolution
res = (1200,800)

# width and height
width = 1200
height = 800

# opens up a window
screen = pygame.display.set_mode(res)

# color
color = (255,0,0)

# light shade of the button
color_light = (144, 140, 135)

# dark shade of the button
color_dark = (13,240,44)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
height = screen.get_height()
# load image
end_screen = pygame.image.load("end_screen.png")
screen.blit(end_screen, (0,0))

# create a font object
font = pygame.font.Font('fonts/DiloWorld-mLJLv.ttf', 40)

# rendering a text written in
# this font
text = font.render('play again' , True , color)
text2 = font.render('exit', True, color)
textRect = text.get_rect()
text2Rect = text2.get_rect()

while True:
	
	for ev in pygame.event.get():
		
		if ev.type == pygame.QUIT:
			pygame.quit()
			
		#checks if a mouse is clicked
		if ev.type == pygame.MOUSEBUTTONDOWN:
			mpos = pygame.mouse.get_pos() # Get mouse position

			print(mpos)
			if text2Rect.collidepoint(mpos):
				pygame.quit()
				
			if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
				Popen('python app.py')
				pygame.quit()	
				
	# fills the screen with a img
	screen.blit(end_screen, (0,0))
	
	# stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()
	
	# superimposing the text onto our button
	tetextRectxt2Rect = screen.blit(text , (width/3+140,height/2))
	text2Rect = screen.blit(text2, (width/3+140,height/1.6))
	
	# updates the frames of the game
	pygame.display.update()

