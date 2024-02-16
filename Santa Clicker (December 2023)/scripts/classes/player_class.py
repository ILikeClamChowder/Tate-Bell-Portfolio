from scripts.settings import *

class Player(pg.sprite.Sprite):

    def __init__(self, x, y):
        super(Player, self).__init__()
        # self.image = pg.Surface(tile_size)
        # self.image.fill(GREEN)
        self.org_img1 = pg.image.load("scripts/assets/sprites/32x32-bat-sprite/image_0-3.png").convert_alpha()
        self.org_img2 = pg.image.load("scripts/assets/sprites/32x32-bat-sprite/image_1-3.png").convert_alpha()
        self.org_img3 = pg.image.load("scripts/assets/sprites/32x32-bat-sprite/image_2-3.png").convert_alpha()
        self.org_img4 = pg.image.load("scripts/assets/sprites/32x32-bat-sprite/image_3-3.png").convert_alpha()
        self.images = [self.org_img1,self.org_img2,self.org_img3, self.org_img4]
        self.anim_index = 0
        self.image = self.images[self.anim_index].copy()
        self.image = self.org_img1.copy()
        self.image = pg.transform.scale(self.image, tile_size)
        self.image.set_colorkey((255,0,255))
        self.can_anim = False
        self.anim_cooldown = 0
        self.anim_dur = 2
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.move_dir_x = 1

    def update(self,dt):
        self.move(1,1)
        if self.can_anim:
            self.animate()
        else:
            self.anim_cooldown -= dt
            if self.anim_cooldown <= 0:
                self.can_anim = True

    def animate(self):
        self.anim_index += 1
        if self.anim_index >= len(self.images):
            self.anim_index = 0
        self.image = self.images[self.anim_index].copy()
        self.image = pg.transform.scale(self.image, tile_size)
        self.image.set_colorkey((255, 0, 255))
        if self.move_dir_x > 0 :
            self.image = pg.transform.flip(self.image,False,False)
        elif self.move_dir_x < 0:
            self.image = pg.transform.flip(self.image,True,False)

        self.anim_cooldown = self.anim_dur
        self.can_anim = False


    def move(self, x, y):
        self.rect.centerx += 1


