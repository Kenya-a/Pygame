README

Is this my first READme

cool. 

anyways heres what we are doing. 

This is literally a spint challenge after a week of learning. 

1. Intro: 
    1. Guess the number in terminal 
    2. Basic understanding of what those commands mean and actually replicating it in the terminal 
    3. 
https://coderslegacy.com/python/python-pygame-tutorial/

Very helpful pygame tutorial. 



Passing pygame.sprite.Sprite into the parameters,makes the Player Class it’s child class. Passing super().init() then calls the init() function of the Sprite class. super().__init__() is a whole different concept related to Classes in Python. You can look it up if you’re interested, else just include it the way we’ve shown above.

Two of the if statements are commented out because this is a side scroller game. We don’t need up and down movement here. 

    P1.update()
    E1.move()
    
    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
        
    pygame.display.update()
    FramePerSec.tick(FPS)

The commands shown above are all in the game loop, so they are repeating continuously. First the update and move functions for both the Enemy and Player class are called.

Next we refresh the screen using the DISPLAY.fill(WHITE) function, finally we call the draw functions for both the Player and Enemy objects, drawing them to the screen.

Finally, the pygame.display.update() command updates the screen with all the commands that have occurred up-till this point, and the tick() makes sure it repeats only 60 times per second.

sololearn is easy way to learn python 

www.sololearn.com
