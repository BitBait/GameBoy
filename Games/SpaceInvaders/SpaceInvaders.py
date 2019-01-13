#Imports
import pygame,sys
from pygame.locals import *

#Classes
class Bullet(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image = pygame.image.load("Bullet.png").convert()
        self.rect = self.image.get_rect()

    def MoveUp(self):
        self.rect.y -= 5

class Ship(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image = pygame.image.load("Ship.png").convert_alpha()
        self.rect = self.image.get_rect()

    def MoveLeft(self):
        self.rect.x -= 10

    def MoveRight(self):
        self.rect.x += 10

    def Nuke(self):
        EnemyGroup.empty()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):

        super().__init__()
        self.image = pygame.image.load("Enemy.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.Direction = "Right"


    def update(self):
        if self.Direction == "Right":
            self.rect.x += 2
        elif self.Direction == "Left":
            self.rect.x -= 2
        if self.rect.x > 467:
            self.rect.y += 30
            self.Direction = "Left"
        elif self.rect.x < 0:
            self.rect.y += 30
            self.Direction = "Right"


class TextRender(pygame.sprite.Sprite):
    def __init__(self):

        self.Level = 1
        super().__init__()
        self.Text = pygame.font.SysFont("", 20)
        self.image = self.Text.render("Level " + str(self.Level) , False, White)
        self.rect = self.image.get_rect()



    def update(self):
        self.image = self.Text.render("Level " + str(self.Level) , False, White)
        self.rect = self.image.get_rect()





#Variables + PygameInit
Width = 500
Height = 500
Resolution = (Width,Height)
pygame.init()
Screen = pygame.display.set_mode(Resolution)
Black = (0, 0, 0)
White = (255, 255, 255)
XCoord = 10
YCoord = 470
ShipInit = Ship()
ShipInit.rect.x = XCoord
ShipInit.rect.y = YCoord
BulletGroup = pygame.sprite.GroupSingle()
ShipGroup = pygame.sprite.GroupSingle()
EnemyGroup = pygame.sprite.Group()
ShipGroup.add(ShipInit)
AllSprites = pygame.sprite.Group()
TextGroup = pygame.sprite.GroupSingle()
HasShot = False
Spawn = True
Cycle = 0
Level = 1
EnemyNumber = 0
Text = TextRender()
TextGroup.add(Text)
HitSound = pygame.mixer.Sound("Hit.ogg")
ShootSound = pygame.mixer.Sound("Shoot.ogg")
UpdateLevel = False
BackGroundSound = pygame.mixer.Sound("BackGround Music.ogg")
BackGroundSound.set_volume(0.1)
BackGroundSound.play(-1)

while True:

    Screen.fill(Black)
    for event in pygame.event.get():
        if event.type == QUIT:
            quit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                quit()
            if event.key == K_RIGHT:
                print("Right")
                ShipInit.MoveRight()
            if event.key == K_LEFT:
                print("Left")
                ShipInit.MoveLeft()
            if event.key == K_UP and HasShot == False:
                ShootSound.play()
                BulletInit = Bullet()
                BulletInit.rect.x = ShipInit.rect.x + 15
                BulletInit.rect.y = ShipInit.rect.y
                BulletGroup.add(BulletInit)
                HasShot = True
            if event.key == K_DOWN:
                ShipInit.Nuke()
                print("Nuke")


    if HasShot == True:
        BulletInit.MoveUp()
        if BulletInit.rect.y == 0:
            HasShot = False
            BulletGroup.empty()

    if Cycle % 40 == 0 and Spawn == True:
        EnemyInit = Enemy()
        EnemyNumber += 1
        EnemyInit.rect.x = 2
        EnemyInit.rect.y = 30
        EnemyGroup.add(EnemyInit)
        if EnemyNumber == 2 * Level:
            Spawn = False
            EnemyNumber = 0
            Level += 1
            TextGroup.update()

    for i in pygame.sprite.groupcollide(EnemyGroup, BulletGroup, True, True):
        print("Hit")
        HitSound.play()

    EnemyGroup.update()

    for i in pygame.sprite.groupcollide(EnemyGroup, ShipGroup, True, True):
        quit()


    if len(EnemyGroup) == 0:
        Spawn = True
        Text.Level = Level
        TextGroup.update()


    BulletGroup.draw(Screen)
    EnemyGroup.draw(Screen)
    AllSprites.add(ShipGroup, TextGroup)
    AllSprites.draw(Screen)
    pygame.time.delay(10)
    Cycle += 1
    pygame.display.flip()
