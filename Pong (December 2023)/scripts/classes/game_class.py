from scripts.settings import *
from scripts.classes.player_class import Player
from scripts.classes.present_class import Paddle

class Game(object):
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.joystick.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.players = pg.sprite.Group()
        self.paddles = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.is_playing = True


        self.player = Player(WIDTH/2, HEIGHT/2)
        self.paddle1 = Paddle(1)
        self.paddle2 = Paddle(2)
        self.paddles.add(self.paddle1)
        self.paddles.add(self.paddle2)
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.paddles)

        self.score = [0,0]



    def update(self):
        self.all_sprites.update(self.clock.tick(FPS))
        for paddle in self.paddles:

            if self.checkOverlarp(self.player,paddle):
                self.player.move_dir_x*=-1

    def play(self):
        while self.is_playing:
            # tick clock
            self.clock.tick(FPS)
            self.get_game_events()
            self.update()
            self.draw()

    def checkOverlarp(self,obj1,obj2):
        if (obj1.rect.left) < (obj2.rect.right):
            if obj2.num == 1:
                if (obj1.rect.left+20) > (obj2.rect.right):
                    if (obj1.rect.top) < (obj2.rect.bottom):
                        if (obj1.rect.bottom) > (obj2.rect.top):
                            return True
        if (obj1.rect.right) > (obj2.rect.left):
            if obj2.num == 2:
                if (obj1.rect.right-20) < (obj2.rect.left):
                    if (obj1.rect.top) < (obj2.rect.bottom):
                        if (obj1.rect.bottom) > (obj2.rect.top):
                            return True
        else:
            return False

    def awardPoint(self, team):
        if team == 1:
            score[0] +=1
        elif team == 2:
            score[1] +=1

    def get_game_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.is_playing = False

    def start_screen(self):
        self.window.fill(WHITE)
        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    return "quit"
                    pg.quit()
                waiting = False

    def end_screen(self):
        print("end")
        return "quit"

    def draw(self):
        self.window.fill(WHITE)
        self.all_sprites.draw(self.window)

        pg.display.flip()

