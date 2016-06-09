import pygame
import tkinter as tk
from tkinter import font as tkfont 

WHITE = (255, 255, 255)

class Eaten:

    def drawEatenCounter(eatenCounter, DISPLAYSURF, WINWIDTH):
    
        BASICFONT = pygame.font.Font('fonts/Kenzo.otf', 20) 
        eatenSurf = BASICFONT.render('EATEN: ', True, WHITE)
        eatenRect = eatenSurf.get_rect()
        eatenRect.center = (WINWIDTH - 50, 30)
        DISPLAYSURF.blit(eatenSurf, eatenRect)
        
        eatenCounterSurf = BASICFONT.render(str(eatenCounter), True, WHITE)
        eatenCounterRect = eatenCounterSurf.get_rect()
        eatenCounterRect.center = (WINWIDTH - 15, 30)
        DISPLAYSURF.blit(eatenCounterSurf, eatenCounterRect)