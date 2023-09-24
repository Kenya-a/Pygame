import pygame, sys, random
from pygame.locals import *
# import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen information
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

#We use classes to be able to spawn multiple entitites from the same block of code. Normally most can will have more enemies than they do players. 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 

        #the image.load() function to which we pass the file path of our image. Note, this does not define the borders for our Player Sprite. We ill be using Collision detection later on. 
        self.image = pygame.image.load("Enemy.png")

        #self.rect.center, defines a starting position for the Rect. Later we’ll use the Rect’s coordinates to draw the image to the exact same location.
        self.rect = self.image.get_rect()

        #The only change is with the last line, where we included randomized starting points. (It would be pretty boring if the Enemy appeared from the same location each time)
        
        self.rect.center=(random.randint(40,SCREEN_WIDTH-40),0) 

      def move(self):
        self.rect.move_ip(0,10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

      def draw(self, surface):
        surface.blit(self.image, self.rect) 


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

#The blit() method takes two inputs, the first the surface to be drawn to and second, the object which we want to draw. Normally we would write surface.blit(self.surf, self.rect) since we’re drawing the rectangle to the surface we’ve defined. But since we’re using an image, we pass self.image instead of self.surf. (An image is in fact, a surface in Pygame)

    def draw(self, surface):
        surface.blit(self.image, self.rect)     

        
P1 = Player()
E1 = Enemy()

while True:     
    for event in pygame.event.get():              
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    P1.update()
    E1.move()
    
    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
        
    pygame.display.update()
    FramePerSec.tick(FPS)