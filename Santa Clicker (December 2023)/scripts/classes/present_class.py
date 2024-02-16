from scripts.settings import *


class Present(pg.sprite.Sprite):

    def __init__(self, game, x, y, price):
        super(Present, self).__init__()

        # self.image = pg.Surface(tile_size)
        # self.image.fill(GREEN)
        self.game = game
        self.imageU = pg.image.load("scripts/assets/sprites/presents.png").convert_alpha()
        self.imageU = pg.transform.scale(self.imageU, tile_size)
        self.imageU.set_colorkey((255,0,255,0))
        self.rect = self.imageU.get_rect()
        self.rect.center = (x,y)
        self.move_dir_y = 1
        self.moveSpeed = 2
        self.rotationSpeed = random.randint(-300,300)/150
        self.rotationAngle = 0
        self.image = ""

        self.ticks = 0
        self.price = price


    def update(self,dt):
        self.ticks +=1
        self.rotationAngle = self.rotationAngle + self.rotationSpeed

        self.moveSpeed = self.ticks * 1.2
        self.image = pg.transform.rotate(self.imageU, self.rotationAngle)
        if self.moveSpeed > 50:
            self.moveSpeed = 50
        if self.rect.y > HEIGHT:
            # add to presents
            self.game.addCurrency(self.price)
            self.kill()



        self.move(0,self.moveSpeed)

        self.animate()


    def animate(self):
        self.imageU.set_colorkey((0, 0, 255, 0.0))
        self.imageU.set_alpha(200)



    def move(self, x, y):
        self.rect.centerx += x
        self.rect.centery += y