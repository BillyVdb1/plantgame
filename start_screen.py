from subprocess import Popen
import pygame




# initializing the constructor
pygame.init()

# screen resolution
res = (900,506)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255,255,255)


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
start_screen = pygame.image.load("start_screen.png")
screen.blit(start_screen, (0,0))
# defining a font
#smallfont = pygame.font.SysFont('Corbel',35)

smallfont = pygame.font.Font('fonts/DiloWorld-mLJLv.ttf', 50)

# rendering a text written in
# this font


text = smallfont.render('start' , True , color)
text2 = smallfont.render('exit', True, color)
text2Rect = text2.get_rect()
textRect = text.get_rect() 





while True:
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
			

		if ev.type == pygame.MOUSEBUTTONDOWN:
			mpos = pygame.mouse.get_pos() # Get mouse position

			print(mpos)
			if text2Rect.collidepoint(mpos):
				pygame.quit()
		
			if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:
				Popen('python app.py')
				pygame.quit()
				
	# fills the screen with a img
	screen.blit(start_screen, (0,0))
	
	# stores the (x,y) coordinates into
	# the variable as a tuple
	mouse = pygame.mouse.get_pos()
	
	# if mouse is hovered on a button it
	# changes to lighter shade
	
	
	# superimposing the text onto our button 
	tetextRectxt2Rect = screen.blit(text , (width/3+140,height/2))
	text2Rect = screen.blit(text2, (width/3+140,height/1.6))
	
	# updates the frames of the game
	pygame.display.update()
