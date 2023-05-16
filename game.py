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
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Variables
SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080

WHITE = (255, 255, 255)

FPS = 60

bulletType = 0
bulletDamage = 0
# Functions

# Drawin on the screen


def drawOnScreeN():
    screen.fill((0, 0, 0))
    screen.blit(player.image, (player.x, player.y))
    for bullet in bullets:
        screen.blit(bullet.image, (bullet.x, bullet.y))
    pygame.display.update()

# Classes


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((100, 100))
        self.image = pygame.transform.scale(pygame.image.load(
            os.path.join("Assets", "player.png")), (100, 100))
        self.rect = self.surf.get_rect()
        self.HP = 100
        self.x = 1
        self.y = SCREEN_HEIGHT / 2
        self.vel = 3

    def update(self, pressed_keys):
        if pressed_keys[K_w]:
            self.y = self.y - self.vel
        if pressed_keys[K_s]:
            self.y = self.y + self.vel
        if pressed_keys[K_a]:
            self.x = self.x - self.vel
        if pressed_keys[K_d]:
            self.x = self.x + self.vel

        if self.x < 0:
            self.x = 0
        if self.x > SCREEN_WIDTH:
            self.x = SCREEN_WIDTH
        if self.y <= 0:
            self.y = 0
        if self.y >= SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT

        # Bullets
        for bullet in bullets:
            if len(bullets) < 5:
                bullets.append(Bullet(self.x, self.y))
                if pressed_keys[K_d] and bullet.x < SCREEN_WIDTH and bullet.x > 0:
                    bullet.x = bullet.x + 1
                else:
                    bullets.pop(bullets.index(bullet))
                if pressed_keys[K_a] and bullet.x < SCREEN_WIDTH and bullet.x > 0:
                    bullet.x = bullet.x - 1
                else:
                    bullets.pop(bullets.index(bullet))
                if pressed_keys[K_w] and bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                    bullet.y = bullet.y - 1
                else:
                    bullets.pop(bullets.index(bullet))
                if pressed_keys[K_s] and bullet.y < SCREEN_HEIGHT and bullet.y > 0:
                    bullet.y = bullet.y + 1
                else:
                    bullets.pop(bullets.index(bullet))


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((50, 50))


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.image = pygame.image.load(os.path.join("Assets", "Bullet.png"))
        self.rect = self.surf.get_rect()
        self.type = bulletType
        self.damage = bulletDamage
        self.vel = 5
        self.x = x
        self.y = y


# Main programing
pygame.init()

bullets = []

player = Player()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

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
