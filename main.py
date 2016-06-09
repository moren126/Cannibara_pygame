import pygame
import time
import random
from game import*
import tkinter as tk
from tkinter import font as tkfont 

WINWIDTH = 800 # szerokosc okna
WINHEIGHT = 600 # wysokosc okna
HALF_WINWIDTH = int(WINWIDTH / 2)
HALF_WINHEIGHT = int(WINHEIGHT / 2)

GROUNDCOLOR = (34, 177, 76)
WHITE = (255,255,255)
RED = (230, 0, 0)
BRIGHT_RED = (255,0,0)


def main():
    global DISPLAYSURF, clock 
    
    pygame.init()   
    pygame.display.set_icon(pygame.image.load('graphics/capybaraUltra.png'))
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Cannibara')  
    
    clock = pygame.time.Clock()
    
    menu()

 
def menu():

    intro = True

    while intro:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        DISPLAYSURF.fill(GROUNDCOLOR)
        BASICFONT = pygame.font.Font('fonts/Kenzo.otf', 120) 
        winSurf = BASICFONT.render('Cannibara', True, WHITE)
        winRect = winSurf.get_rect()
        winRect.center = (HALF_WINWIDTH, HALF_WINHEIGHT - 180)
        DISPLAYSURF.blit(winSurf, winRect)

        logoSurf = pygame.image.load('graphics/capybaraUltra.png')
        DISPLAYSURF.blit(logoSurf, (HALF_WINWIDTH - 168, HALF_WINHEIGHT - 125))
        
        playButton("Play",100,450,100,50,RED,BRIGHT_RED)
        quitButton("Quit",600,450,100,50,RED,BRIGHT_RED)

        pygame.display.update()
        clock.tick(15)
 
   
def playButton(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(DISPLAYSURF, ac,(x,y,w,h))
        
        if click[0] == 1:
            Game.runGame(WINWIDTH,WINHEIGHT,DISPLAYSURF)   
        
    else:
        pygame.draw.rect(DISPLAYSURF, ic,(x,y,w,h))

    BASICFONT2 = pygame.font.Font('fonts/Kenzo Regular Italic.otf', 30)    

    winSurf2 = BASICFONT2.render('PLAY', True, WHITE)
    winRect2 = winSurf2.get_rect()
    winRect2.center = ( (x+(w/2)), (y+(h/2)) )
    DISPLAYSURF.blit(winSurf2, winRect2)     
    
    
def quitButton(msg,x,y,w,h,ic,ac):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(DISPLAYSURF, ac,(x,y,w,h))
        
        if click[0] == 1:
            quitgame()   
        
    else:
        pygame.draw.rect(DISPLAYSURF, ic,(x,y,w,h))

    BASICFONT2 = pygame.font.Font('fonts/Kenzo Regular Italic.otf', 30)    

    winSurf2 = BASICFONT2.render('QUIT', True, WHITE)
    winRect2 = winSurf2.get_rect()
    winRect2.center = ( (x+(w/2)), (y+(h/2)) )
    DISPLAYSURF.blit(winSurf2, winRect2)  
                   
        
def quitgame():
    pygame.quit()
    quit()

    
if __name__ == '__main__':
    main()