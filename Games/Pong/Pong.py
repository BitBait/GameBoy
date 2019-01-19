#Imports
import pygame,sys
from pygame.locals import *

#Classes
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        self.speedX = 1
        self.speedY = 1

        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(White)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.speedX
        self.rect.y += self.speedY

class Player(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image = pygame.Surface([10,50])
        self.image.fill(White)
        self.rect = self.image.get_rect()

    def MoveUp(self):
        self.rect.y += 2

    def MoveDown(self):
        self.rect.y -= 2

#Variables
Black = (0, 0, 0)
White = (255, 255, 255)
Width = 800
Height = 350
Resolution = (Width,Height)
pygame.init()
Screen = pygame.display.set_mode(Resolution)
BallInit = Ball()
BallInit.rect.x = 20
BallInit.rect.y = 50
BallGroup = pygame.sprite.GroupSingle()
BallGroup.add(BallInit)
PlayerOne = Player()
PlayerOne.rect.x = 0
PlayerOne.rect.y = 250
PlayerTwo = Player()
PlayerTwo.rect.x = 790
PlayerTwo.rect.y = 250
PlayerOneGroup = pygame.sprite.GroupSingle()
PlayerOneGroup.add(PlayerOne)
PlayerTwoGroup = pygame.sprite.GroupSingle()
PlayerTwoGroup.add(PlayerTwo)
AllSpritesGroup = pygame.sprite.Group()
Cycle = 0
Rally = 1

while True:
    Screen.fill(Black)

    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
            '''
            if event.key == K_DOWN:
                PlayerOne.MoveUp()
            if event.key == K_UP:
                PlayerOne.MoveDown()
            if event.key == K_w:
                PlayerTwo.MoveDown()
            if event.key == K_s:
                PlayerTwo.MoveUp()
            '''
    key = pygame.key.get_pressed()
    if key[K_UP]:
        PlayerOne.MoveDown()
    if key[K_DOWN]:
        PlayerOne.MoveUp()
    if key[K_w]:
        PlayerTwo.MoveDown()
    if key[K_s]:
        PlayerTwo.MoveUp()


    if BallInit.rect.x < 0:
        BallInit.rect.x = 400
        Rally = 1
        pygame.time.delay(1000)
        BallInit.speedX = 1
        BallInit.speedY = 1

    if BallInit.rect.x > 800:
        BallInit.rect.x = 400
        Rally = 1
        pygame.time.delay(1000)
        BallInit.speedX = 1
        BallInit.speedY = 1

    if BallInit.rect.y < 0 or BallInit.rect.y > 350:
        BallInit.speedY = -BallInit.speedY

    #if Rally % 5 == 0:
        #BallInit.speedX += 1
        #BallInit.speedY += 1

    BallGroup.update()
    if pygame.sprite.groupcollide(BallGroup, PlayerOneGroup, False, False):
        BallInit.speedX = -BallInit.speedX
        Rally += 1
    if pygame.sprite.groupcollide(BallGroup, PlayerTwoGroup, False, False):
        BallInit.speedX = -BallInit.speedX
        Rally += 1

    AllSpritesGroup.add(PlayerOneGroup,PlayerTwoGroup,BallGroup)
    AllSpritesGroup.draw(Screen)
    pygame.display.flip()
    pygame.time.delay(5)






