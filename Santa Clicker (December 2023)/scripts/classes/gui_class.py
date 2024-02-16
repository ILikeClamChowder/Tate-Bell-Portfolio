from scripts.settings import *

class GUI(pg.sprite.Sprite):

    def __init__(self, type, x, y, sizeX, sizeY, color):
        super(GUI, self).__init__()
        self.xpos = x
        self.ypos = y
        self.width = sizeX
        self.height = sizeY
        self.type = type
        self.color = color
        self.xSpeed = random.randint(0, 10)
        self.ySpeed = random.randint(0, 10)
        self.event = False
        self.t = (self.width, self.height)



        if self.type == "santa":
            self.image = pg.image.load("scripts/assets/sprites/santa.png")
            self.image = self.image.copy()
            self.image = pg.transform.scale(self.image, self.t)

        if self.type == "cannon":
            self.image = pg.image.load("scripts/assets/sprites/cannon.png")
            self.image = self.image.copy()
            self.image = pg.transform.scale(self.image, self.t)
            self.image.set_colorkey((255, 255, 255, 0.0))

        if self.type != "santa" and self.type != "cannon":
            self.image = pg.Surface(self.t)
            self.image.fill(color)


            pg.display.flip()


        self.rect = self.image.get_rect()
        self.rect.center = (self.xpos, self.ypos)


    def move(self):
        self.xpos += self.xSpeed
        self.ypos += self.ySpeed
        self.rect = self.image.get_rect()
        self.rect.center = (self.xpos, self.ypos)
        if self.xpos >= WIDTH-375:
            self.xSpeed = abs(self.xSpeed)*-1
            self.image = pg.transform.flip(self.image, True, False)
        elif self.xpos <= 50:
            self.xSpeed = abs(self.xSpeed)
            self.image = pg.transform.flip(self.image, True, False)

        if self.ypos >= HEIGHT-50:
            self.ySpeed = abs(self.ySpeed)*-1
        elif self.ypos <= 250:
            self.ySpeed = abs(self.ySpeed)


        if random.randint(1,25) == 1:
            temp = self.xSpeed
            if self.event == True:
                self.xSpeed = 2 * random.randint(-10, 10)
            else:
                self.xSpeed = random.randint(-10, 10)
            if (temp >= 0 and self.xSpeed >= 0) or (temp <= 0 and self.xSpeed <= 0):
                return
            self.image = pg.transform.flip(self.image, True, False)

        if random.randint(1,25) == 1:
            temp = self.ySpeed
            if self.event == True:
                self.ySpeed = 2 * random.randint(-10, 10)
            else:
                self.ySpeed = random.randint(-10, 10)


    def cannonMove(self):
        self.ypos += 1
        self.rect.center = (self.xpos, self.ypos)
        self.rect = self.image.get_rect()
        if ypos == 100:
            self.ypos += 0
            return True
















