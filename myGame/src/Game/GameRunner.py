import sys
from pygame.locals import *
from GameLoader import *


def run():
    loader = GameLoader()
    screen = loader.screen()
    ljx = loader.images().get("background")
    while 1:
        for event in pygame.event.get():
            if event.type in (QUIT, KEYDOWN):
                sys.exit()
        screen.blit(ljx, (0, 0))
        pygame.display.update()
        pygame.time.delay(1000)
