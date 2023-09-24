#Import begins
    # here we import pygame and modules into our rogram. 
    #the secome line allows us to use the function and variables in the pygame.locals moduel with out having to add lenthy prefix

import pygame
import sys
from pygame.locals import *


# init() function initializes the pygame engine, if you don't have this the game will not run. \

pygame.init()

#The Game Loop
    #In this loop all game events will occur, update, and get drawn onto the screen. Program keeps looping over and over until an event type QUIT  occurs. Therefore, it will run infinitely. 
    #pygame.display.update() is responsible for updating the game window with any changes made during a specific iteration of the game loop.  

while True:
        #do this

        pygame.display.update()

#Quitting the game loop

while True: 
        for event in pygame.event.get(): 
            if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
        pygame.display.update()

 # pygame.quit() and sys.exit() will close the pygame window and python script respectively. We are able to use the sys module because we imported it    

 #Event Objects in Pygame
    # An "event" occurs when the user performs a specific action such as clicking a mouse or pressing a key. We can find out which event have happened by calling pygame.event.get() function



#Creating a Display screen

DISPLAYSURF = pygame.display.set_mode((300,300))

#Pygame Colors 
 #pygame reads colors in RBG values, which come in tuple format. 

color1 = pygame.Color(0,0,0)        #BLACK
color2 = pygame.Color(255,255,255)  #WHITE
color3 = pygame.Color(128,128,128)  #GREY
color4 = pygame.Color(255,0,0)      #RED


#Setting Frames per second

FPS = pygame.time.Clock()
Fps.tick(60)

#How do you explain FPS AND HOW YOU DEFINED IT. 

#Recognizing Collision in Pygame. 
    #here we are defining boundaries. 

object1 = pygame.Rect((20,50),(50,100))
object2 = pygame.Rect((10,10)(100,100))

print(object1.colliderect(object2))
# We can test for a rect based on the coordinates on the screen.