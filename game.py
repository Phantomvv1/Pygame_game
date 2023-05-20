import pygame
import os
import random

from pygame.locals import (
    K_w,
    K_a,
    K_s,
    K_d,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    MOUSEBUTTONDOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
GREY = (128, 128 , 128)
BROWN = (160, 82, 45)

FPS = 60

def game(bulletType, bulletDamage):
    # Variables
    bulletType = bulletType
    bulletDamage = bulletDamage
    # Functions

    # Drawin on the screen


    def drawOnScreeN():
        screen.fill(BROWN)
        screen.blit(player.image, (player.x, player.y))
        for bullet in bullets:
            screen.blit(bullet.image, (bullet.x, bullet.y))
        pygame.display.update()

    # Classes


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.image = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "player.png")), (100, 100))
            self.rect = self.image.get_rect()
            self.HP = 100
            self.rect.width = 100
            self.rect.height = 100
            self.x = SCREEN_WIDTH / 2 - self.rect.width
            self.y = SCREEN_HEIGHT / 2 - self.rect.height
            self.vel = 4
            self.invincible = False
            

        def update(self, pressed_keys):
            if pressed_keys[K_w]:
                self.y = self.y - self.vel
            if pressed_keys[K_s]:
                self.y = self.y + self.vel
            if pressed_keys[K_a]:
                self.x = self.x - self.vel
            if pressed_keys[K_d]:
                self.x = self.x + self.vel

            if self.x <= 0:
                self.x = 0
            if self.x >= SCREEN_WIDTH - self.rect.width:
                self.x = SCREEN_WIDTH - self.rect.width
            if self.y <= 0:
                self.y = 0
            if self.y >= SCREEN_HEIGHT - self.rect.height:
                self.y = SCREEN_HEIGHT - self.rect.height

            # Bullets
            if pressed_keys[K_RIGHT]:
                bullets.append(Bullet(self.x, self.y))
                if len(bullets) < 5 and len(bullets) > 0:
                    for bullet in bullets:
                        if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                            bullet.x = bullet.x + 1
                        else:
                            bullets.pop(bullets.index(bullet))
                else:
                    bullets.pop(bullets.index(bullet))
            
            if pressed_keys[K_LEFT]:
                bullets.append(Bullet(self.x, self.y))
                if len(bullets) < 5 and len(bullets) > 0:
                    for bullet in bullets:
                        if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                            bullet.x = bullet.x - 1
                        else:
                            bullets.pop(bullets.index(bullet))
                else:
                    bullets.pop(bullets.index(bullet))
            
            if pressed_keys[K_UP]:
                bullets.append(Bullet(self.x, self.y))
                if len(bullets) < 5 and len(bullets) > 0: 
                    for bullet in bullets:
                        if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                            bullet.y = bullet.y - 1
                        else:
                            bullets.pop(bullets.index(bullet))
                else:
                    bullets.pop(bullets.index(bullet))

            if pressed_keys[K_DOWN]:
                bullets.append(Bullet(self.x, self.y))
                if len(bullets) < 5 and len(bullets) > 0:
                    for bullet in bullets:
                        if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                            bullet.y = bullet.y + 1
                        else:
                            bullets.pop(bullets.index(bullet))
                else:
                    bullets.pop(bullets.index(bullet))


    class Enemy(pygame.sprite.Sprite):
        def __init__(self):
            super(Enemy, self).__init__()
            self.surf = pygame.Surface((50, 50))
            self.image
            self.rect = self.image.get_rect()
            self.HP = 100
            self.rect.width = 100
            self.rect.height = 100
            self.x
            self.y


    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(Bullet, self).__init__()
            self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Rock.png")), (50, 50))
            self.rect = self.image.get_rect()
            self.type = bulletType
            self.damage = bulletDamage
            self.vel = 20
            self.x = x
            self.y = y
        

    # Main programing
    pygame.init()

    bullets = []

    player = Player()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption("Game")

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            elif event.type == QUIT:
                running = False

        drawOnScreeN()

        pressed_keys = pygame.key.get_pressed()

        player.update(pressed_keys)


def updates(coins):
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    clock = pygame.time.Clock()

    smallfont = pygame.font.SysFont(None, 35)

    bigfont = pygame.font.SysFont(None, 70)

    textCoins = bigfont.render(f"Coins: {coins}", True, BLACK)

    textUpgrades = smallfont.render("Updates", True, BLACK)

    textMenu = smallfont.render("Menu", True, WHITE)

    textWeapons = smallfont.render("Weapons:", True, BLACK)

    textHealth = smallfont.render("Health:", True, BLACK)

    textSpeed = smallfont.render("Speed:", True, BLACK)

    textBought = smallfont.render("Bought:", True, BLACK)

    textHPp25 = bigfont.render("+25", True, BLACK)

    textHPp50 = bigfont.render("+50", True, BLACK)

    textHPp75 = bigfont.render("+75", True, BLACK)

    textHPp100 = bigfont.render("+100", True, BLACK)

    AK47 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "AK_47.png")), (350, 100))
    Wand = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Wand.jpg")), (100, 100))
    Slingshot = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Slingshot.png")), (100, 100))
    Bazooka = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Bazooka.png")), (200, 100))
    AK47bought = False
    Wandbought = False
    Slingshotbought = True
    Bazookabought = False
    HPp25 = False
    HPp50 = False
    HPp75 = False
    HPp100 = False

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(CYAN)
        pygame.draw.rect(screen, BLACK, [SCREEN_WIDTH / 2 - 140 + 50, SCREEN_HEIGHT - 60, 140, 40])
        screen.blit(textCoins, (20, 100))
        screen.blit(textWeapons, (20, 300))
        screen.blit(textHealth, (20, 450))
        screen.blit(textSpeed, (20, 600))
        screen.blit(textMenu,(SCREEN_WIDTH / 2 - 140 + 85, SCREEN_HEIGHT - 50))
        screen.blit(textUpgrades, (SCREEN_WIDTH / 2 - 100, 100))
        screen.blit(AK47, (350, 275))
        screen.blit(Wand, (700 + 50, 275))
        screen.blit(Bazooka, (750 + 150, 275))
        screen.blit(Slingshot, (200 , 275))
        screen.blit(textHPp25, (200, 450))
        screen.blit(textHPp50, (350, 450))
        screen.blit(textHPp75, (500, 450))
        screen.blit(textHPp100, (650, 450))

        #Showing the bought items
        if Slingshotbought == True:
            screen.blit(textBought, (200, 250))
            if AK47bought == True:
                screen.blit(textBought, (350 + 87, 250))
                if Wandbought == True:
                    screen.blit(textBought, (750, 250))
                    if Bazookabought == True:
                        screen.blit(textBought, (900 + 50, 250))

        if HPp25 == True:
            screen.blit(textBought, (200, 425))
            if HPp50 == True:
                screen.blit(textBought, (350, 425))
                if HPp75 == True:
                    screen.blit(textBought, (500, 425))
                    if HPp100 == True:
                        screen.blit(textBought, (650, 425))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get(): 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    pygame.quit()
            elif event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                    #Buying guns
                    if 350 <= mouse[0] <= 700 and 275 <= mouse[1] <= 375 and coins >= 1000:
                        coins = coins - 1000
                        AK47bought = True
                    if 750 <= mouse[0] <= 850 and 275 <= mouse[1] <= 375 and coins >= 2000 and AK47bought == True:
                        coins = coins - 2000
                        Wandbought = True
                    if 900 <= mouse[0] <= 1100 and 275 <= mouse[1] <= 375 and coins >= 5000 and Wandbought == True:
                        coins = coins - 5000
                        Bazookabought = True
                    #Buying HP
                    if 200 <= mouse[0] <= 270 and 450 <= mouse[1] <= 520 and coins >= 1000:
                        coins = coins - 1000
                        HPp25 = True
                    if 350 <= mouse[0] <= 420 and 450 <= mouse[1] <= 520 and coins >= 2000 and HPp25 == True:
                        coins = coins - 2000
                        HPp50 = True
                    if 500 <= mouse[0] <= 570 and 450 <= mouse[1] <= 520 and coins >= 5000 and HPp50 == True:
                        coins = coins - 5000
                        HPp75 = True
                    if 650 <= mouse[0] <= 720 and 450 <= mouse[1] <= 520 and coins >= 10000 and HPp75 == True:
                        coins = coins - 10000
                        HPp100 = True
                    if SCREEN_WIDTH / 2 - 140 + 50 <= mouse[0] <= SCREEN_WIDTH / 2 + 50 and SCREEN_HEIGHT - 60 <= mouse[1] <= SCREEN_HEIGHT - 60 + 40:
                        menu()
            

        pygame.display.update()


def menu():
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    clock = pygame.time.Clock()

    smallfont = pygame.font.SysFont(None, 35) 

    textQuit = smallfont.render("Quit", True, WHITE)

    textTitle = smallfont.render("Bullet Bonanza", True, BLACK)

    textUpgrades = smallfont.render("Updates", True, WHITE)

    textPlay = smallfont.render("Play", True, WHITE)

    running = True
    while running:
        clock.tick(FPS)
        screen.fill(CYAN)
        pygame.draw.rect(screen, BLACK, [SCREEN_WIDTH / 2 - 140 + 50, SCREEN_HEIGHT / 2 + 50, 140, 40])
        pygame.draw.rect(screen, BLACK, [SCREEN_WIDTH / 2 - 140 + 50, SCREEN_HEIGHT / 2, 140, 40])
        pygame.draw.rect(screen, BLACK, [SCREEN_WIDTH / 2 - 140 + 50, SCREEN_HEIGHT / 2 - 50, 140, 40])
        screen.blit(textQuit, (SCREEN_WIDTH / 2 - 140 + 40 + 50, SCREEN_HEIGHT / 2 + 60))
        screen.blit(textUpgrades, (SCREEN_WIDTH / 2 - 140 + 40 + 30, SCREEN_HEIGHT / 2 + 10))
        screen.blit(textPlay, (SCREEN_WIDTH / 2 - 140 + 40 + 55, SCREEN_HEIGHT / 2 - 60 + 20))
        screen.blit(textTitle,(SCREEN_WIDTH / 2 - 100, 100))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get(): 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    pygame.quit()
            elif event.type == QUIT:
                running = False
                pygame.quit()

            if event.type == MOUSEBUTTONDOWN:
                if SCREEN_WIDTH / 2 - 140 + 50 <= mouse[0] <= SCREEN_WIDTH / 2 + 50 and SCREEN_HEIGHT / 2 + 50 <= mouse[1] <= SCREEN_HEIGHT / 2 + 40 + 50: 
                    running = False
                if SCREEN_WIDTH / 2 - 140 + 50 <= mouse[0] <= SCREEN_WIDTH / 2 + 50 and SCREEN_HEIGHT / 2 <= mouse[1] <= SCREEN_HEIGHT / 2 + 40: 
                    updates(10000)
                if SCREEN_WIDTH / 2 - 140 + 50 <= mouse[0] <= SCREEN_WIDTH / 2 + 50 and SCREEN_HEIGHT / 2 - 50 <= mouse[1] <= SCREEN_HEIGHT / 2 + 40 - 50: 
                    game(0, 0)


        pygame.display.update()


def readFile():
    exists = os.path.isfile("Pregress.txt")
    if exists == True:
        with open("Progress.txt", "r") as progress:
            exists = True
    else:
        with open("Progress.txt", "w"):
            exists = True

menu()