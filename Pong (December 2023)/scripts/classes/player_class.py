from scripts.settings import *

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        super(Player, self).__init__()
        # self.image = pg.Surface(tile_size)
        # self.image.fill(GREEN)
        self.image = pg.image.load("scripts/assets/sprites/dvd.png").convert_alpha()
        self.image = pg.transform.scale(self.image, tile_size)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, random.randrange(100,HEIGHT-100))
        self.move_dir_x = -1
        self.move_dir_y = 1

        self.speed = 10

    def update(self,dt):
        self.move(1,1)

    



    def move(self, x, y):

        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.move_dir_y = self.move_dir_y * -1

        if self.rect.left < 0:
            #self.game.awardPoint(1)
            self.rect.center = (WIDTH / 2, random.randrange(100,HEIGHT-100))
            self.move_dir_x *= -1
        elif self.rect.right > WIDTH:
            #self.game.awardPoint(2)
            self.rect.center = (WIDTH / 2, random.randrange(100, HEIGHT-100))
            self.move_dir_x*=-1


        

        


        self.rect.centerx += self.speed * self.move_dir_x
        self.rect.centery += self.speed * self.move_dir_y

