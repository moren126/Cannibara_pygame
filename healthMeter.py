import pygame

WHITE = (255, 255, 255)
RED = (230, 0, 0)

class HealthMeter:

    def drawHealthMeter(currentHealth, DISPLAYSURF, MAXHEALTH):
        for i in range(currentHealth): 
            pygame.draw.rect(DISPLAYSURF, RED,   (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10))
        for i in range(MAXHEALTH):
            pygame.draw.rect(DISPLAYSURF, WHITE, (15, 5 + (10 * MAXHEALTH) - i * 10, 20, 10), 1)