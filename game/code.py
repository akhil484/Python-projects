import pygame
import sys
from pygame.locals import *
import random

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen information
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

DISPLAYSURF = pygame.display.set_mode((500, 500))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("newball.png")
        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)
        self.speed_x = 0
        self.speed_y = 5

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.bottom > 600 or self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed_x *= -1

    def reverse_direction(self):
        self.speed_y *= -1
        self.speed_x *= -1

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sledg.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-4, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(4, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


P1 = Player(250, 20)
P2 = Player(250, 480)
b = Ball()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    P1.update()
    P2.update()
    b.move()

    # Collision detection
    if b.rect.colliderect(P1.rect) or b.rect.colliderect(P2.rect):
        b.reverse_direction()
    
    DISPLAYSURF.fill(BLUE)
    # P1.draw(DISPLAYSURF)
    # P2.draw(DISPLAYSURF)
    pygame.draw.rect(DISPLAYSURF, BLACK, P1.rect)  # Draw P1's rect
    pygame.draw.rect(DISPLAYSURF, BLACK, P2.rect)
    # pygame.draw.rect(DISPLAYSURF, BLACK, b.rect)
    b.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)