
from scripts.settings import *
from scripts.classes.controller_class import *
from scripts.classes.player_class import Player
from scripts.classes.present_class import Present
from scripts.classes.gui_class import GUI
from scripts.classes.elf_class import Elf
from scripts.classes.particle_class import Particle

class Game(object):
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.joystick.init()
        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.players = pg.sprite.Group()
        self.all_sprites = pg.sprite.Group()
        self.bg = pg.image.load("scripts/assets/sprites/backgroundimg1.jpg")
        self.bg = pg.transform.scale(self.bg, (WIDTH,HEIGHT))

        self.is_playing = True
        # self.controllers = []
        # try:
        #    pg.joystick.init()
        #    joy_count = pg.joystick.get_count()
        #    if joy_count > 0:
        #        for i in range(joy_count):
        #            self.controllers.append(Controller(i))
        # except:
        #    print("testing")
        #self.player = Player(WIDTH/2, HEIGHT/2)
        #self.player.add(self.players)
        # self.all_sprites.add(self.player)

        self.presentsCurrency = 0
        self.upgMultiplier = 1
        self.upgPrice = 40
        self.elfAmount = 0
        self.elfPrice = 15
        self.elfTicks = 0
        self.upgElfAmount = 1
        self.upgElfPrice = 100
        self.eventActive = False

        self.presents = pg.sprite.Group()
        self.elves = pg.sprite.Group()
        self.createGUIS()

        for i in range(1,10):
            for button in self.buttons:
                if button.type == "santa":
                    particle = Particle(self, button.xpos, button.ypos, "corn")
                    self.all_sprites.add(particle)


    # def getVar(self,var):
    #
    #     return "var"

    def teleportParticles(self , particle):
        for button in self.buttons:
            if button.type == "santa":
                particle.move(button.xpos,button.ypos)
                particle.ticks = 0
                particle.image.set_alpha(0)

    def spawnCandyCane(self): #we needa FIX THIS GANG WHY IS SOURCE OBJECT NOT A SURFACE
        for i in range(1,10):
            particle = Particle(self, WIDTH/2, 0, "cane")
            self.all_sprites.add(particle)

    def checkEvent(self):
        if self.eventActive:
            return True
        else:
            return False



    def addCurrency(self, amount):
        self.presentsCurrency += amount*self.upgMultiplier

    def addElfCurrency(self,amount):
        self.presentsCurrency += amount*self.upgElfAmount

    def purchaseUpg(self):
        if self.presentsCurrency >= self.upgPrice:
            self.presentsCurrency -= self.upgPrice
            self.upgMultiplier *=2
            self.upgPrice *= 2.15

    def spawnPresent(self):
        for button in self.buttons:
            if button.type == "santa":
                xPos = button.xpos
                yPos = button.ypos
        if self.eventActive == True:
            present = Present(self,xPos, yPos, 5)
        else:
            present = Present(self, xPos, yPos, 1)
        self.presents.add(present)
        self.all_sprites.add(present)

    def sillyEvent(self):
        temp = 0
        if random.randint(1,3600) == 1:
            print("silly event :33333")
            self.eventActive=True
            # self.spawnCandyCane()
            for button in self.buttons:
                if button.type == "santa":
                    button.event = True

        if self.eventActive == True:
            temp = temp+1
            if temp >= 600:
                self.eventActive = False
                button.event = False


    def createGUIS(self):
        self.buttons = pg.sprite.Group()
        presentsDisplay = GUI("presentsDisplay", WIDTH / 2, 150, WIDTH, 50, WHITE)
        self.buttons.add(presentsDisplay)
        nameDisplay = GUI("nameDisplay", WIDTH / 2, 50, WIDTH, 100, WHITE)
        self.buttons.add(nameDisplay)
        santa = GUI("santa", WIDTH/2, HEIGHT/2, 100, 89, BLACK)
        self.buttons.add(santa)
        upgButton = GUI("upgButton", WIDTH-175, 250, 300, 100, WHITE)
        self.buttons.add(upgButton)
        elf = GUI("elf", WIDTH - 175, 375, 300, 100, WHITE)
        self.buttons.add(elf)
        upgElf = GUI("upgElf", WIDTH - 175, 500, 300, 100, WHITE)
        self.buttons.add(upgElf)





        self.all_sprites.add(self.buttons)


    def spawnElf(self):
        cannon = GUI("cannon", 25, HEIGHT-30, 100, 100, BLUE)
        self.buttons.add(cannon)

        if self.presentsCurrency >= self.elfPrice:
            self.presentsCurrency -= self.elfPrice
            self.elfPrice *= 1.15
            if self.elfAmount >= 0:
                self.elfAmount +=1
                elf = Elf(self, 1, HEIGHT, "elf")
                self.all_sprites.add(elf)
                self.elves.add(elf)


    def elfSantaCollision(self):
        for button in self.buttons:
            if button.type == "santa":
                pass
                for elf in self.elves:
                    xval = False
                    yval = False
                    if (elf.rect.right >= button.xpos) and (elf.rect.left <= button.xpos+button.width):
                        xval = True
                    if (elf.rect.bottom >= button.ypos) and (elf.rect.top <= button.ypos+button.height):
                        yval = True

                    if xval == True and yval == True:
                        if elf.touchy == False:
                            self.addElfCurrency(1)
                            elf.touchy = True



    def spawnCoal(self):
        coal = Elf(self, 1, HEIGHT, "coal")
        self.all_sprites.add(coal)

    def upgElfPurchase(self):
        if self.presentsCurrency >= self.upgElfPrice:
            self.presentsCurrency -= self.upgElfPrice
            self.upgElfAmount *= 2
            self.upgElfPrice *=2.1





    def update(self):
        self.all_sprites.update(self.clock.tick(FPS))
        self.mouseOverlap()
        self.sillyEvent()
        self.elfSantaCollision()
        # self.elfTick()
        for button in self.buttons:
            if button.type == "santa":
                button.move()




    def draw(self):
        self.window.fill(WHITE)
        self.window.blit(self.bg, (0,0))
        self.all_sprites.draw(self.window)
        self.presents.draw(self.window)
        self.buttons.draw(self.window)
        self.guiText()
        pg.display.flip()

    def guiText(self):
        button_transparency = 100
        for button in self.buttons:
            if button.type == "presentsDisplay":
                button.image.fill((255,255,255,0))
                button.image.set_alpha(100)
                draw_text(button.image, "presents: "+str(math.floor(self.presentsCurrency)), 20, BLACK, button.width / 2, button.height / 4, "segoeuisemibold")
            elif button.type == "nameDisplay":
                button.image.fill((255, 255, 255, 0))
                button.image.set_alpha(100)
                draw_text(button.image, "Santa Clicker", 40, BLACK, button.width / 2,button.height / 5, "segoeuisemibold")
            elif button.type == "upgButton":
                button.image.fill((WHITE))
                button.image.set_alpha(button_transparency)
                draw_text(button.image, "Upgrade the clicker", 20, BLACK, button.width / 2, button.height / 4, "segoeuisemibold")
                draw_text(button.image, str(math.ceil(self.upgPrice)) + " presents", 20, BLACK,
                          button.width / 2, (button.height / 4) + 25,
                          "segoeuisemibold")
            elif button.type == "elf":
                button.image.fill((WHITE))
                button.image.set_alpha(button_transparency)
                draw_text(button.image, "Hire Elves to get presents", 20, BLACK, button.width / 2, button.height / 4,
                          "segoeuisemibold")
                draw_text(button.image, str(math.ceil(self.elfPrice)) + " presents", 20, BLACK,
                          button.width / 2, (button.height / 4) + 25,
                          "segoeuisemibold")
            elif button.type == "upgElf":
                button.image.fill((WHITE))
                button.image.set_alpha(button_transparency)
                draw_text(button.image, "Make your Elves work harder", 20, BLACK, button.width / 2, button.height / 4,
                          "segoeuisemibold")
                draw_text(button.image, str(math.ceil(self.upgElfPrice))+" presents", 20, BLACK,
                          button.width / 2, (button.height / 4) + 25,
                          "segoeuisemibold")

    def play(self):
        while self.is_playing:
            # tick clock
            self.clock.tick(FPS)


            self.get_game_events()
            self.update()
            self.draw()

    def mouseOverlap(self):
        for button in self.buttons:
            self.mouse_pos = pg.mouse.get_pos()
            self.mouse_bttns = pg.mouse.get_pressed()
            x = False
            y = False
            if self.mouse_pos[0] < button.xpos + button.width/2 and self.mouse_pos[0] > button.xpos-button.width/2:
                x=True
            if self.mouse_pos[1] < button.ypos + button.height/2 and self.mouse_pos[1] > button.ypos-button.height/2:
                y=True

            if x and y == True:
                return button.type
            else:
                continue




    def get_game_events(self):
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                self.is_playing = False
            if event.type == pg.MOUSEBUTTONDOWN:
                mousePos = pg.mouse.get_pos()
                if self.mouseOverlap() == "santa":
                    self.spawnPresent()
                elif self.mouseOverlap() == "upgButton":
                    self.purchaseUpg()
                elif self.mouseOverlap() == "upgElf":
                    self.upgElfPurchase()
                elif self.mouseOverlap() == "elf":
                    self.spawnElf()
                elif self.mouseOverlap() == "cannon":
                    self.spawnCoal()
                else:
                    pass
                    # print(self.mouseOverlap())





    def start_screen(self):
        self.window.fill(BLACK)
        draw_screen("scripts/assets/sprites/backgroundimg.jpg", 0, 0, self.window)
        draw_text(self.window, "Santa Simulator", 60, WHITE, WIDTH / 2, HEIGHT / 2)

        pg.display.flip()
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            events = pg.event.get()
            for event in events:
                if event.type == pg.QUIT:
                    return "quit"
                    pg.quit()
                if event.type == pg.MOUSEBUTTONDOWN:
                        waiting = False
                        print("no longer waiting")

    def end_screen(self):
        print("end")
        return "quit"


