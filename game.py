import time
import sys
import pygame
from pygame.locals import*
import tkinter as tk
from tkinter import font as tkfont 

from ground import*
from enemy import*
from bouncing import*
from healthMeter import *
from eaten import *

FPS = 30
WINWIDTH = 800 # szerokosc okna
WINHEIGHT = 600 # wysokosc okna
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

GROUNDCOLOR = (34, 177, 76)
WHITE = (255, 255, 255)
RED = (230, 0, 0)
PURPLE = (153, 0, 204)

CAMERASLACK = 90
MOVERATE = 9
BOUNCERATE = 6
BOUNCEHEIGHT = 30
STARTSIZE = 40
WINSIZE = 400
INVULNTIME = 2
GAMEOVERTIME = 4
MAXHEALTH = 3

NUMGROUND = 80
NUMCAPS = 30
CAPMINSPEED = 3
CAPMAXSPEED = 7
DIRCHANGEFREQ = 2
LEFT = 'left'
RIGHT = 'right'

class Game:

    def runGame(WINWIDTH,WINHEIGHT,DISPLAYSURF):

        FPSCLOCK = pygame.time.Clock()
        L_CAP_IMG = pygame.image.load('graphics/capybara.png')
        R_CAP_IMG = pygame.transform.flip(L_CAP_IMG, True, False)    

        # audio 
        pygame.mixer.music.load('sounds/capybara_sound_mono.wav')
        pygame.mixer.music.play(-1)

        # ustawienie zmiennych na nową rozgrywkę
        invulnerableMode = False
        invulnerableStartTime = 0
        gameOverMode = False
        gameOverStartTime = 0
        winMode = False

        # powierzchnie na teksty gry
        BASICFONTG = pygame.font.Font('fonts/Kenzo.otf', 70) 
        gameOverSurf = BASICFONTG.render('Game Over', True, PURPLE)
        gameOverRect = gameOverSurf.get_rect()
        gameOverRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

        BASICFONTW = pygame.font.Font('fonts/Kenzo.otf', 48) 
        winSurf = BASICFONTW.render('You have become ultra CANNIBAL CAPYBARA!', True, WHITE)
        winRect = winSurf.get_rect()
        winRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT)

        BASICFONTI = pygame.font.Font('fonts/Kenzo Regular Italic.otf', 48)  
        winSurf2 = BASICFONTI.render('(Press "m" to go to menu)', True, WHITE)
        winRect2 = winSurf2.get_rect()
        winRect2.center = (HALF_WINWIDTH, HALF_WINHEIGHT + 40)

        # licznik zjedzonych kapibar
        eatens = 0
             
        camerax = 0
        cameray = 0

        groundObjs = []     # podłoże
        enemyObjs = []      # przeciwnicy
        
        # gracz
        playerObj = {'surface': pygame.transform.scale(L_CAP_IMG, (STARTSIZE, STARTSIZE)),
                     'facing': LEFT,
                     'size': STARTSIZE,
                     'x': HALF_WINWIDTH,
                     'y': HALF_WINHEIGHT,
                     'bounce':0,
                     'health': MAXHEALTH}

        moveLeft  = False
        moveRight = False
        moveUp    = False
        moveDown  = False

        for i in range(10):
            groundObjs.append(Ground.makeNewGround(camerax, cameray, WINWIDTH, WINHEIGHT))
            groundObjs[i]['x'] = random.randint(0, WINWIDTH)
            groundObjs[i]['y'] = random.randint(0, WINHEIGHT)

        # główna pętla gry    
        while True:
        
            # sprawdzenie czy wyłączyć nietykalność gracza
            if invulnerableMode and time.time() - invulnerableStartTime > INVULNTIME:
                invulnerableMode = False


            for eObj in enemyObjs:

                eObj['x'] += eObj['movex']
                eObj['y'] += eObj['movey']
                eObj['bounce'] += 1
                if eObj['bounce'] > eObj['bouncerate']:
                    eObj['bounce'] = 0

                if random.randint(0, 99) < DIRCHANGEFREQ:
                    eObj['movex'] = Enemy.getRandomVelocity(CAPMINSPEED,CAPMAXSPEED)
                    eObj['movey'] = Enemy.getRandomVelocity(CAPMINSPEED,CAPMAXSPEED)
                    if eObj['movex'] > 0:
                        eObj['surface'] = pygame.transform.scale(R_CAP_IMG, (eObj['width'], eObj['height']))
                    else:
                        eObj['surface'] = pygame.transform.scale(L_CAP_IMG, (eObj['width'], eObj['height']))

                        
            for i in range(len(groundObjs) - 1, -1, -1):
                if Camera.isOutsideActiveArea(camerax, cameray, groundObjs[i], WINWIDTH, WINHEIGHT):
                    del groundObjs[i]
            for i in range(len(enemyObjs) - 1, -1, -1):
                if Camera.isOutsideActiveArea(camerax, cameray, enemyObjs[i], WINWIDTH, WINHEIGHT):
                    del enemyObjs[i]


            while len(groundObjs) < NUMGROUND:
                groundObjs.append(Ground.makeNewGround(camerax, cameray, WINWIDTH, WINHEIGHT))
            while len(enemyObjs) < NUMCAPS:
                enemyObjs.append(Enemy.makeNewEnemy(camerax, cameray, L_CAP_IMG, R_CAP_IMG, CAPMINSPEED, CAPMAXSPEED, WINWIDTH, WINHEIGHT))


            playerCenterx = playerObj['x'] + int(playerObj['size'] / 2)
            playerCentery = playerObj['y'] + int(playerObj['size'] / 2)
            if (camerax + HALF_WINWIDTH) - playerCenterx > CAMERASLACK:
                camerax = playerCenterx + CAMERASLACK - HALF_WINWIDTH
            elif playerCenterx - (camerax + HALF_WINWIDTH) > CAMERASLACK:
                camerax = playerCenterx - CAMERASLACK - HALF_WINWIDTH
            if (cameray + HALF_WINHEIGHT) - playerCentery > CAMERASLACK:
                cameray = playerCentery + CAMERASLACK - HALF_WINHEIGHT
            elif playerCentery - (cameray + HALF_WINHEIGHT) > CAMERASLACK:
                cameray = playerCentery - CAMERASLACK - HALF_WINHEIGHT

            # dorysowanie reszty podłoża 
            DISPLAYSURF.fill(GROUNDCOLOR)

            # rysowanie obiektów podłoża na ekranie
            for gObj in groundObjs:
                gRect = pygame.Rect( (gObj['x'] - camerax,
                                      gObj['y'] - cameray,
                                      gObj['width'],
                                      gObj['height']) )
                DISPLAYSURF.blit(GROUNDIMAGES[gObj['groundImage']], gRect)


            # rysowanie wrogich kapibar
            for eObj in enemyObjs:
                eObj['rect'] = pygame.Rect( (eObj['x'] - camerax,
                                             eObj['y'] - cameray - Bouncing.getBounceAmount(eObj['bounce'], eObj['bouncerate'], eObj['bounceheight']),
                                             eObj['width'],
                                             eObj['height']) )
                DISPLAYSURF.blit(eObj['surface'], eObj['rect'])


            # rysowanie gracza
            flashIsOn = round(time.time(), 1) * 10 % 2 == 1
            if not gameOverMode and not (invulnerableMode and flashIsOn):
                playerObj['rect'] = pygame.Rect( (playerObj['x'] - camerax,
                                                  playerObj['y'] - cameray - Bouncing.getBounceAmount(playerObj['bounce'], BOUNCERATE, BOUNCEHEIGHT),
                                                  playerObj['size'],
                                                  playerObj['size']) )
                DISPLAYSURF.blit(playerObj['surface'], playerObj['rect'])


            # rysowanie wskaźnika poziomu zdrowia
            HealthMeter.drawHealthMeter(playerObj['health'], DISPLAYSURF, MAXHEALTH, WINHEIGHT)

            # rysowanie licznika zjedzonych kapibar
            Eaten.drawEatenCounter(eatens, DISPLAYSURF, WINWIDTH)
            
            # obsługa zdarzeń
            for event in pygame.event.get():
                if event.type == QUIT:
                    Game.terminate()

                elif event.type == KEYDOWN:
                    # znak, że trzeba wprawić gracza w ruch
                    if event.key in (K_UP, K_w):
                        moveDown = False
                        moveUp = True
                    elif event.key in (K_DOWN, K_s):
                        moveUp = False
                        moveDown = True
                    elif event.key in (K_LEFT, K_a):
                        moveRight = False
                        moveLeft = True
                        if playerObj['facing'] != LEFT:
                            playerObj['surface'] = pygame.transform.scale(L_CAP_IMG, (playerObj['size'], playerObj['size']))
                        playerObj['facing'] = LEFT
                    elif event.key in (K_RIGHT, K_d):
                        moveLeft = False
                        moveRight = True
                        if playerObj['facing'] != RIGHT:
                            playerObj['surface'] = pygame.transform.scale(R_CAP_IMG, (playerObj['size'], playerObj['size']))
                        playerObj['facing'] = RIGHT
                    elif winMode and event.key == K_m:
                        return

                elif event.type == KEYUP:
                    # zatrzymanie ruchu gracza
                    if event.key in (K_LEFT, K_a):
                        moveLeft = False
                    elif event.key in (K_RIGHT, K_d):
                        moveRight = False
                    elif event.key in (K_UP, K_w):
                        moveUp = False
                    elif event.key in (K_DOWN, K_s):
                        moveDown = False

                    elif event.key == K_ESCAPE:
                        terminate()

            if not gameOverMode:
                # ruszanie gracza w odpowiednim kierunku
                if moveLeft:
                    playerObj['x'] -= MOVERATE
                if moveRight:
                    playerObj['x'] += MOVERATE
                if moveUp:
                    playerObj['y'] -= MOVERATE
                if moveDown:
                    playerObj['y'] += MOVERATE

                if (moveLeft or moveRight or moveUp or moveDown) or playerObj['bounce'] != 0:
                    playerObj['bounce'] += 1

                if playerObj['bounce'] > BOUNCERATE:
                    playerObj['bounce'] = 0

                # sprawdzanie kolizji z wrogimi kapibarami
                for i in range(len(enemyObjs)-1, -1, -1):
                    enObj = enemyObjs[i]
                    if 'rect' in enObj and playerObj['rect'].colliderect(enObj['rect']):
                    
                        # doszło do kolizji
                        if enObj['width'] * enObj['height'] <= playerObj['size']**2:
                            # gracz jt większy i zjada kapibarę
                            eatens += 1
                            playerObj['size'] += int( (enObj['width'] * enObj['height'])**0.2 ) + 1
                            del enemyObjs[i]

                            if playerObj['facing'] == LEFT:
                                playerObj['surface'] = pygame.transform.scale(L_CAP_IMG, (playerObj['size'], playerObj['size']))
                            if playerObj['facing'] == RIGHT:
                                playerObj['surface'] = pygame.transform.scale(R_CAP_IMG, (playerObj['size'], playerObj['size']))

                            if playerObj['size'] > WINSIZE:
                                winMode = True

                        elif not invulnerableMode:
                            # gracz jt mniejszy i traci zdrowie
                            injured = pygame.mixer.Sound('sounds/capybara_barks_mono.wav')
                            injured.play()
                            invulnerableMode = True
                            invulnerableStartTime = time.time()
                            playerObj['health'] -= 1
                            if playerObj['health'] == 0:
                                gameOverMode = True
                                gameOverStartTime = time.time()
            else:
                # koniec gry
                DISPLAYSURF.blit(gameOverSurf, gameOverRect)
                pygame.mixer.music.fadeout(1000)
                if time.time() - gameOverStartTime > GAMEOVERTIME:
                    return

            # sprawdzenie czy gracz wygrał
            if winMode:
                DISPLAYSURF.blit(winSurf, winRect)
                DISPLAYSURF.blit(winSurf2, winRect2)
                pygame.mixer.music.fadeout(1000)
                #pygame.mixer.music.stop()

            pygame.display.update()
            FPSCLOCK.tick(FPS)
            
            
    def terminate():
        pygame.quit()
        sys.exit()