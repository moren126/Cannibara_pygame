import pygame
from game import*

WINWIDTH = 800 # szerokosc okna
WINHEIGHT = 600 # wysokosc okna

def main():
    
    pygame.init()   
    pygame.display.set_icon(pygame.image.load('graphics/capybaraUltra.png'))
    DISPLAYSURF = pygame.display.set_mode((WINWIDTH, WINHEIGHT))
    pygame.display.set_caption('Cannibara')  
    
    while True:
        Game.runGame(WINWIDTH,WINHEIGHT,DISPLAYSURF)

if __name__ == '__main__':
    main()