from typing import Any
import pygame
import os
import time

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

def game(coins, AK47bought, Wandbought, Bazookabought, HPp25, HPp50, HPp75, HPp100, Speedp025, Speedp050, Speedp075, Speedp1):
    # Variables
    enemiesKilled = 0
    startSpawn = True
    timePassed = 0
    # Functions

    # Drawin on the screen


    def drawOnScreeN():
        nonlocal startSpawn
        screen.fill(BROWN)
        screen.blit(player.image, (player.x, player.y))
        if enemiesKilled > 0 and enemiesKilled % 4 == 0 or startSpawn == True:
            startSpawn = False
            enemies.append(Enemy(1, SCREEN_HEIGHT / 2))
            enemies.append(Enemy(SCREEN_WIDTH - 101, SCREEN_HEIGHT / 2))
            enemies.append(Enemy(SCREEN_WIDTH / 2, 1))
            enemies.append(Enemy(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 101))
        for enemy in enemies:
            screen.blit(enemy.image, (enemy.x, enemy.y))
        pygame.display.update()

    # Classes


    class Player(pygame.sprite.Sprite):
        def __init__(self):
            super(Player, self).__init__()
            self.image = pygame.transform.scale(pygame.image.load(
                os.path.join("Assets", "player.png")), (100, 100))
            self.rect = self.image.get_rect()
            if HPp25 == False:
                self.HP = 100
            if HPp25 == True and HPp50 == False:
                self.HP = 125
            if HPp50 == True and HPp75 == False:
                self.HP = 150
            if HPp75 == True and HPp100 == False:
                self.HP = 175
            if HPp100 == True:
                self.HP = 200
            self.rect.width = 100
            self.rect.height = 100
            self.x = SCREEN_WIDTH / 2 - self.rect.width
            self.y = SCREEN_HEIGHT / 2 - self.rect.height
            if Speedp025 == False:
                self.vel = 4
            if Speedp025 == True and Speedp050 == False:
                self.vel = 4.25
            if Speedp050 == True and Speedp075 == False:
                self.vel = 4.5
            if Speedp075 == True and Speedp1 == False:
                self.vel = 4.75
            if Speedp1 == True:
                self.vel = 5
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
                            screen.blit(bullet.image, (bullet.x, bullet.y))
                        else:
                            bullets.pop(bullets.index(bullet))
            
            if pressed_keys[K_LEFT]:
                bullets.append(Bullet(self.x, self.y))
                if len(bullets) < 5 and len(bullets) > 0:
                    for bullet in bullets:
                        if bullet.x < SCREEN_WIDTH and bullet.x > 0:
                            bullet.x = bullet.x - 1
                            screen.blit(bullet.image, (bullet.x, bullet.y))
                        else:
                            bullets.pop(bullets.index(bullet))
            
            if pressed_keys[K_UP]:
                bullets.append(Bullet(self.x, self.y))
                if len(bullets) < 5 and len(bullets) > 0: 
                    for bullet in bullets:
                        if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                            bullet.y = bullet.y - 1
                            screen.blit(bullet.image, (bullet.x, bullet.y))
                        else:
                            bullets.pop(bullets.index(bullet))

            if pressed_keys[K_DOWN]:
                bullets.append(Bullet(self.x, self.y))
                if len(bullets) < 5 and len(bullets) > 0:
                    for bullet in bullets:
                        if bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                            bullet.y = bullet.y + 1
                            screen.blit(bullet.image, (bullet.x, bullet.y))
                        else:
                            bullets.pop(bullets.index(bullet))


    class Enemy(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(Enemy, self).__init__()
            self.surf = pygame.Surface((100, 100))
            self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Enemy.png")), (100, 100))
            self.rect = self.image.get_rect()
            self.HP = 100
            self.rect.width = 100
            self.rect.height = 100
            self.x = x
            self.y = y
            self.vel = 3

        def update(self, player):
            if self.x <= 0:
                self.x = 0
            if self.x >= SCREEN_WIDTH - self.rect.width:
                self.x = SCREEN_WIDTH - self.rect.width
            if self.y <= 0:
                self.y = 0
            if self.y >= SCREEN_HEIGHT - self.rect.height:
                self.y = SCREEN_HEIGHT - self.rect.height

            if player.x < self.x and self.x > player.x + 75:
                self.x = self.x - self.vel
            if player.x > self.x and self.x < player.x + 75:
                self.x = self.x + self.vel
            if player.y > self.y and self.y < player.y + 75:
                self.y = self.y + self.vel
            if player.y < self.y and self.y > player.y + 75:
                self.y = self.y - self.vel

            #Checking if the enemy has touched the player
            nonlocal timePassed
            if player.x <= self.x <= player.x + 90 and player.y <= self.y <= player.y + 90 and player.invincible == False:
                timePassed = time.time()
                player.invincible = True
                player.HP = player.HP - 25
            if timePassed + 1 <= time.time():
                player.invincible = False


    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            super(Bullet, self).__init__()
            if AK47bought == False:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Rock.png")), (50, 50))
                self.rect = self.image.get_rect()
                self.damage = 35
            if AK47bought == True and Wandbought == False:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Bullet.png")), (50, 50))
                self.rect = self.image.get_rect()
                self.damage = 50
            if Wandbought == True and Bazookabought == False:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Wand_bullet.png")), (50, 50))
                self.rect = self.image.get_rect()
                self.damage = 75
            if Bazookabought == True:
                self.image = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Rocket.png")), (50, 50))
                self.rect = self.image.get_rect()
                self.damage = 100
            self.vel = 20
            self.x = x
            self.y = y
            

    # Main programing
    pygame.init()

    bullets = []

    enemies = []

    player = Player()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    pygame.display.set_caption("Bullet Bonanza")

    clock = pygame.time.Clock()
    running = True
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    coins = coins + 20 * enemiesKilled
                    menu(coins, AK47bought, Wandbought, Bazookabought, HPp25, HPp50, HPp75, HPp100, Speedp025, Speedp050, Speedp075, Speedp1)
            elif event.type == QUIT:
                running = False

        if player.HP <= 0:
            running = False
            coins = coins + 20 * enemiesKilled
            menu(coins, AK47bought, Wandbought, Bazookabought, HPp25, HPp50, HPp75, HPp100, Speedp025, Speedp050, Speedp075, Speedp1)

        drawOnScreeN()
        
        pressed_keys = pygame.key.get_pressed()

        player.update(pressed_keys)

        for enemy in enemies:
            enemy.update(player)


def updates(coins, AK47bought, Wandbought, Bazookabought, HPp25, HPp50, HPp75, HPp100, Speedp025, Speedp050, Speedp075, Speedp1):
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

    textSpeedp025 = bigfont.render("+0,25", True, BLACK)

    textSpeedp050 = bigfont.render("+0,50", True, BLACK)

    textSpeedp075 = bigfont.render("+0,75", True, BLACK)

    textSpeedp1 = bigfont.render("+1", True, BLACK)

    textNote1 = smallfont.render("Note that the Health and Speed values are added", True, BLACK)
    textNote2 = smallfont.render("to the original value of the parameter", True, BLACK)

    textPrice1 = smallfont.render("The prices of the items are as it follows:", True, BLACK)
    textPrice2 = smallfont.render("first item: 1000 coins", True, BLACK)
    textPrice3 = smallfont.render("second item: 2000 coins", True, BLACK)
    textPrice4 = smallfont.render("third item: 5000coins", True, BLACK)
    textPrice5 = smallfont.render("fourth item: 10000 coins", True, BLACK)

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
    Speedp025 = False
    Speedp050 = False
    Speedp075 = False
    Speedp1 = False

    pygame.display.set_caption("Bullet Bonanza")
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
        screen.blit(textSpeedp025, (200, 600))
        screen.blit(textSpeedp050, (350, 600))
        screen.blit(textSpeedp075, (500, 600))
        screen.blit(textSpeedp1, (650, 600))
        screen.blit(textNote1, (1200, 400))
        screen.blit(textNote2, (1200, 430))
        screen.blit(textPrice1, (1200, 550))
        screen.blit(textPrice2, (1200, 580))
        screen.blit(textPrice3, (1200, 610))
        screen.blit(textPrice4, (1200, 640))
        screen.blit(textPrice5, (1200, 670))

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
        
        if Speedp025 == True:
           screen.blit(textBought, (200, 575))
           if Speedp050 == True:
               screen.blit(textBought, (350, 575))
               if Speedp075 == True:
                   screen.blit(textBought, (500, 575))
                   if Speedp1 == True:
                       screen.blit(textBought, (650, 575))

        mouse = pygame.mouse.get_pos()

        for event in pygame.event.get(): 
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
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
                    #Buying speed
                    if 200 <= mouse[0] <= 320 and 600 <= mouse[1] <= 670 and coins >= 1000:
                        coins = coins - 1000
                        Speedp025 = True
                    if 350 <= mouse[0] <= 470 and 600 <= mouse[1] <= 670 and coins >= 2000 and Speedp025 == True:
                        coins = coins - 2000
                        Speedp050 = True
                    if 500 <= mouse[0] <= 620 and 600 <= mouse[1] <=670 and coins >= 5000 and Speedp050 == True:
                        coins = coins - 5000
                        Speedp075 = True
                    if 650 <= mouse[0] <= 720 and 600 <= mouse[1] <=670 and coins >= 10000 and Speedp075 == True:
                        coins = coins - 10000
                        Speedp1 = True
                    if SCREEN_WIDTH / 2 - 140 + 50 <= mouse[0] <= SCREEN_WIDTH / 2 + 50 and SCREEN_HEIGHT - 60 <= mouse[1] <= SCREEN_HEIGHT - 60 + 40:
                        running = False
                        menu(coins, AK47bought, Wandbought, Bazookabought, HPp25, HPp50, HPp75, HPp100, Speedp025, Speedp050, Speedp075, Speedp1)
            

        pygame.display.update()


def writeFile(coins, AK47bought, Wandbought, Bazookabought, HPp25, HPp50, HPp75, HPp100, Speedp025, Speedp050, Speedp075, Speedp1):
    with open("Progress.txt", "w") as file:
        file.write(f"Coins = {coins}\n")
        file.write(f"AK47bought = {AK47bought}\n")
        file.write(f"Wandbought = {Wandbought}\n")
        file.write(f"Bazookabought = {Bazookabought}\n")
        file.write(f"HPp25 = {HPp25}\n")
        file.write(f"HPp50 = {HPp50}\n")
        file.write(f"HPp75 = {HPp75}\n")
        file.write(f"HPp100 = {HPp100}\n")
        file.write(f"Speedp025 = {Speedp025}\n")
        file.write(f"Speedp50 = {Speedp050}\n")
        file.write(f"Speedp075 = {Speedp075}\n")
        file.write(f"Speedp1 = {Speedp1}\n")


def menu(coins, AK47bought, Wandbought, Bazookabought, HPp25, HPp50, HPp75, HPp100, Speedp025, Speedp050, Speedp075, Speedp1):
    pygame.init()

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    clock = pygame.time.Clock()

    smallfont = pygame.font.SysFont(None, 35) 

    textQuit = smallfont.render("Quit", True, WHITE)

    textTitle = smallfont.render("Bullet Bonanza", True, BLACK)

    textUpgrades = smallfont.render("Updates", True, WHITE)

    textPlay = smallfont.render("Play", True, WHITE)

    pygame.display.set_caption("Bullet Bonanza")
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
            elif event.type == QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                if SCREEN_WIDTH / 2 - 140 + 50 <= mouse[0] <= SCREEN_WIDTH / 2 + 50 and SCREEN_HEIGHT / 2 + 50 <= mouse[1] <= SCREEN_HEIGHT / 2 + 40 + 50: 
                    running = False
                if SCREEN_WIDTH / 2 - 140 + 50 <= mouse[0] <= SCREEN_WIDTH / 2 + 50 and SCREEN_HEIGHT / 2 <= mouse[1] <= SCREEN_HEIGHT / 2 + 40:
                    running = False
                    updates(coins, AK47bought, Wandbought, Bazookabought, HPp25, HPp50, HPp75, HPp100, Speedp025, Speedp050, Speedp075, Speedp1)
                if SCREEN_WIDTH / 2 - 140 + 50 <= mouse[0] <= SCREEN_WIDTH / 2 + 50 and SCREEN_HEIGHT / 2 - 50 <= mouse[1] <= SCREEN_HEIGHT / 2 + 40 - 50:
                    running = False
                    game(coins, AK47bought, Wandbought, Bazookabought, HPp25, HPp50, HPp75, HPp100, Speedp025, Speedp050, Speedp075, Speedp1)


        pygame.display.update()


def readFile():
    exists = os.path.isfile("Progress.txt")
    if exists == True:
        with open("Progress.txt", "r") as file:
            coins = file.readline().split(" ")[2].replace("\n", "")
            AK47bought = file.readline().split(" ")[2].replace("\n", "")
            Wandbought = file.readline().split(" ")[2].replace("\n", "")
            Bazookabought = file.readline().split(" ")[2].replace("\n", "")
            HPp25 = file.readline().split(" ")[2].replace("\n", "")
            HPp50 = file.readline().split(" ")[2].replace("\n", "")
            HPp75 = file.readline().split(" ")[2].replace("\n", "")
            HPp100 = file.readline().split(" ")[2].replace("\n", "")
            Speedp025 = file.readline().split(" ")[2].replace("\n", "")
            Speedp050 = file.readline().split(" ")[2].replace("\n", "")
            Speedp075 = file.readline().split(" ")[2].replace("\n", "")
            Speedp1 = file.readline().split(" ")[2].replace("\n", "")
            coins = int(coins)
            #Making the guns variables bools
            if AK47bought == "True":
                AK47bought = True
            else:
                AK47bought = False    
            if Wandbought == "True":
                Wandbought = True
            else:
                Wandbought = False    
            if Bazookabought == "True":
                Bazookabought = True
            else:
                Bazookabought = False
                
            #Making the HP variables bools
            if HPp25 == "True":
                HPp25 = True
            else:
                HPp25 = False    
            if HPp50 == "True":
                HPp50 = True
            else:
                    HPp50 = False    
            if HPp75 == "True":
                HPp75 = True
            else:
                HPp75 = False    
            if HPp100 == "True":
                HPp100 = True
            else:
                HPp100 = False
                
            #Making the speed variables bools
            if Speedp025 == "True":
                Speedp025 = True
            else:
                Speedp025 = False    
            if Speedp050 == "True":
                Speedp050 = True
            else:
                Speedp050 = False    
            if Speedp075 == "True":
                Speedp075 = True
            else:
                Speedp075 = False    
            if Speedp1 == "True":
                Speedp1 = True
            else:
                Speedp1 == False    

        menu(coins, AK47bought, Wandbought, Bazookabought, HPp25, HPp50, HPp75, HPp100, Speedp025, Speedp050, Speedp075, Speedp1)
    else:
        writeFile(0 ,False, False, False, False, False, False, False, False, False, False, False)
        readFile()


readFile()