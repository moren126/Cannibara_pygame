import random
from camera import *

class Enemy:

    def getRandomVelocity(CAPMINSPEED, CAPMAXSPEED):
        speed = random.randint(CAPMINSPEED, CAPMAXSPEED)
        if random.randint(0, 1) == 0:
            return speed
        else:
            return -speed

    def makeNewEnemy(camerax, cameray, L_CAP_IMG, R_CAP_IMG, CAPMINSPEED, CAPMAXSPEED,  WINWIDTH, WINHEIGHT):
    
        enemy = {}
        generalSize = random.randint(10, 35)
        multiplier = random.randint(1, 3)
        enemy['width']  = (generalSize + random.randint(0, 10)) * multiplier
        enemy['height'] = (generalSize + random.randint(0, 10)) * multiplier
        enemy['x'], enemy['y'] = Camera.getRandomOffCameraPos(camerax, cameray, enemy['width'], enemy['height'], WINWIDTH, WINHEIGHT)
        enemy['movex'] = Enemy.getRandomVelocity(CAPMINSPEED, CAPMAXSPEED)
        enemy['movey'] = Enemy.getRandomVelocity(CAPMINSPEED, CAPMAXSPEED)
        
        if enemy['movex'] < 0:
            enemy['surface'] = pygame.transform.scale(L_CAP_IMG, (enemy['width'], enemy['height']))
        else:
            enemy['surface'] = pygame.transform.scale(R_CAP_IMG, (enemy['width'], enemy['height']))
            
        enemy['bounce'] = 0
        enemy['bouncerate'] = random.randint(10, 18)
        enemy['bounceheight'] = random.randint(10, 50)
        return enemy