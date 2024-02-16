import math

from scripts.settings import *


class Elf(pg.sprite.Sprite):

    def __init__(self, game, x, y, type):
        super(Elf, self).__init__()

        # self.image = pg.Surface(tile_size)
        # self.image.fill(GREEN)
        self.game = game
        self.type = type
        if self.type == "elf":
            self.imageU = pg.image.load("scripts/assets/sprites/elf.png").convert_alpha()
        else:
            self.imageU = pg.image.load("scripts/assets/sprites/coal.png").convert_alpha()
        self.imageU = pg.transform.scale(self.imageU, tile_size)
        self.rect = self.imageU.get_rect()
        self.rect.center = (x,y)
        self.move_dir_x = 1
        self.move_dir_y = 1

        self.x = x
        self.y = y
        self.moveSpeed = (-1/2 * random.uniform(0, 4) * math.log(self.x + math.e, math.e))
        self.rotationSpeed = random.randint(-10,10)
        self.rotationAngle = 0
        self.image = ""

        self.ticks = 0
        self.ticks2 = 0
        self.touchy = False

    def update(self,dt):
        self.ticks +=1
        self.ticks2 +=1
        if self.ticks2 >= 120:
            if self.type == "elf":
                self.touchy = False
                self.x = 1
                self.y = HEIGHT
                self.moveSpeed = (-1/2 * random.uniform(0, 4) * math.log(self.x + math.e, math.e))
                self.rect.center = (self.x, self.y)
                self.rotationSpeed = random.randint(-10, 10)
                self.rotationAngle = 0
                self.ticks2 = 0
            else:
                self.kill()




        self.rotationAngle = self.rotationAngle + self.rotationSpeed
        self.image = pg.transform.rotate(self.imageU, self.rotationAngle)
        if self.moveSpeed > 50:
            self.moveSpeed = 50




        self.move(2,self.moveSpeed)

        self.animate()


    def animate(self):
        self.imageU.set_colorkey((0, 0, 255, 0.0))
        self.imageU.set_alpha(200)



    def move(self, x, y):
        temp = 10
        self.rect.centerx += x*temp
        self.rect.centery += y*temp
