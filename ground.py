from camera import *

class Ground:

    global GROUNDIMAGES
    
    GROUNDIMAGES = []
    for i in range(1, 5):
        GROUNDIMAGES.append(pygame.image.load('graphics/ground0%s.png' % i))

    def makeNewGround(camerax, cameray, WINWIDTH, WINHEIGHT):
        gr = {}
        gr['groundImage'] = random.randint(0, len(GROUNDIMAGES) - 1)
        gr['width']  = GROUNDIMAGES[0].get_width()
        gr['height'] = GROUNDIMAGES[0].get_height()
        gr['x'], gr['y'] = Camera.getRandomOffCameraPos(camerax, cameray, gr['width'], gr['height'], WINWIDTH, WINHEIGHT)
        gr['rect'] = pygame.Rect( (gr['x'], gr['y'], gr['width'], gr['height']) )
        return gr