import random
import math 
import pygame

class Camera:

    def getRandomOffCameraPos(camerax, cameray, objWidth, objHeight, WINWIDTH, WINHEIGHT):
    
        cameraRect = pygame.Rect(camerax, cameray, WINWIDTH, WINHEIGHT)
        while True:
            x = random.randint(camerax - WINWIDTH, camerax + (2 * WINWIDTH))
            y = random.randint(cameray - WINHEIGHT, cameray + (2 * WINHEIGHT))

            objRect = pygame.Rect(x, y, objWidth, objHeight)
            if not objRect.colliderect(cameraRect):
                return x, y
                
    def isOutsideActiveArea(camerax, cameray, obj, WINWIDTH, WINHEIGHT):

        boundsLeftEdge = camerax - WINWIDTH
        boundsTopEdge = cameray - WINHEIGHT
        boundsRect = pygame.Rect(boundsLeftEdge, boundsTopEdge, WINWIDTH * 3, WINHEIGHT * 3)
        objRect = pygame.Rect(obj['x'], obj['y'], obj['width'], obj['height'])
        return not boundsRect.colliderect(objRect)