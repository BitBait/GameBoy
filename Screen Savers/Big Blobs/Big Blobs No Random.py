import pygame,sys
from pygame.locals import *
from random import randint

Resolution = (500,500)
pygame.init()
Screen = pygame.display.set_mode(Resolution)
Black = (0, 0, 0)
White = (255, 255, 255)
AllSprites = pygame.sprite.Group()
Cycles = 0
Coordinates = []

def ColourGen():
    a = randint(0, 255)
    b = randint(0, 255)
    c = randint(0, 255)
    return (a, b, c)

class Block(pygame.sprite.Sprite):
    def __init__(self, Width, Height, Colour):
        self.Colour = Colour
        super().__init__()
        self.image = pygame.Surface([Width, Height])
        self.image.fill(Colour)
        self.rect = self.image.get_rect()

while True:
    Screen.fill(Black)
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
    x = randint(0, 500)
    y = randint(0, 500)
    Coord = [x,y]

    if len(Coordinates) == 500000:
        Coordinates.clear()

    while Coord in Coordinates:
        Coord[0] = randint(0, 500)
        Coord[1] = randint(0, 500)

    Coordinates.append(Coord)
    print(len(Coordinates))

    if Cycles == 0 or Cycles % 1750 == 0:
        BlockColour = ColourGen()

    BlockInit = Block(10, 10, BlockColour)
    BlockInit.rect.x = x
    BlockInit.rect.y = y
    AllSprites.add(BlockInit)
    AllSprites.draw(Screen)
    pygame.display.flip()
    Cycles += 1