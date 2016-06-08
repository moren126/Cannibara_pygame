import pygame

RED = (230, 0, 0)

class HealthMeter:

    def drawHealthMeter(currentHealth, DISPLAYSURF, MAXHEALTH, WINHEIGHT):
      
        for i in range(currentHealth): 
        
            heartVertices = [ 
            (20 + ( MAXHEALTH - i - 1 ) * 30 , WINHEIGHT - 15), 
            (10 + ( MAXHEALTH - i - 1 ) * 30 , WINHEIGHT - 30), 
            (15 + ( MAXHEALTH - i - 1 ) * 30 , WINHEIGHT - 35), 
            (20 + ( MAXHEALTH - i - 1 ) * 30 , WINHEIGHT - 30), 
            (25 + ( MAXHEALTH - i - 1 ) * 30 , WINHEIGHT - 35), 
            (30 + ( MAXHEALTH - i - 1 ) * 30 , WINHEIGHT - 30)]
        
            pygame.draw.polygon(DISPLAYSURF, RED, heartVertices)