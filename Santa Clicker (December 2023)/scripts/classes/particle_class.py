from scripts.settings import *


class Particle(pg.sprite.Sprite):

    def __init__(self, game, x, y, type):
        super(Particle, self).__init__()

        # self.image = pg.Surface(tile_size)
        # self.image.fill(GREEN)
        self.game = game
        self.type = type
        if self.type == "corn":
            self.imageU = pg.image.load("scripts/assets/sprites/candycorn.png").convert_alpha()
        else:
            self.imageU = pg.image.load("scripts/assets/sprites/candycane.png").convert_alpha()
        self.imageU = pg.transform.scale(self.imageU, tile_size)
        self.imageU.set_colorkey((255,0,255))
        self.rect = self.imageU.get_rect()
        self.rect.center = (x,y)
        self.move_dir_y = 1
        self.moveSpeed = 2
        self.rotationSpeed = random.randint(-300,300)/150
        self.rotationAngle = 0
        self.image = ""

        self.ticks = 0
        self.randUpdate = random.randint(5,50)

    def update(self, dt):
        if self.type == "corn":
            self.ticks +=1
            self.rotationAngle = self.rotationAngle + self.rotationSpeed
            self.image = pg.transform.rotate(self.imageU, self.rotationAngle)
            self.image.set_alpha(255-self.ticks*5)
            if self.ticks == self.randUpdate:
                self.game.teleportParticles(self)
                self.randUpdate = random.randint(5,50)
        if self.type == "cane":
            self.rotationAngle = self.rotationAngle + self.rotationSpeed
            self.image = pg.transform.rotate(self.imageU, self.rotationAngle)
            self.image.set_alpha(140)
            self.rect.centery += 5
            if self.rect.top == HEIGHT:
                if self.game.checkEvent():
                    self.rect.bottom = 0
                else:
                    self.kill()








        self.animate()


    def animate(self):
        self.imageU.set_colorkey((0, 0, 255, 0.0))



    def move(self, x, y):
        self.rect.centerx = x
        self.rect.centery = y