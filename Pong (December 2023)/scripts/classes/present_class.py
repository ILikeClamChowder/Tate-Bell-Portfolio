from scripts.settings import *

class Paddle(pg.sprite.Sprite):

    def __init__(self,num):
        super(Paddle, self).__init__()
        self.image = pg.Surface(tile_size)
        self.rect = self.image.get_rect()
        self.image = pg.image.load("scripts/assets/sprites/pong.jpg").convert_alpha()
        self.image = pg.transform.scale(self.image, (tile_size[0]*0.5,tile_size[1]*2))
        self.rect = self.image.get_rect()
        self.num = num
        if self.num == 1:
            self.rect.center = (tile_size[0]*0.5, HEIGHT/2)
        else:
            self.rect.center = (tile_size[0]*7.5, HEIGHT / 2)

        self.speed=10

    def update(self,dt):


        keyStates = pg.key.get_pressed()


        if self.num == 2:
            if keyStates[pg.K_UP]:
                self.move_dir_y = -1
            elif keyStates[pg.K_DOWN]:
                self.move_dir_y = 1
            else:
                self.move_dir_y = 0
        else:
            if keyStates[pg.K_w]:
                self.move_dir_y = -1
            elif keyStates[pg.K_s]:
                self.move_dir_y = 1
            else:
                self.move_dir_y = 0

        self.rect.centery += self.speed * self.move_dir_y

    def animate(self):
        pass

    def move(self):
        pass