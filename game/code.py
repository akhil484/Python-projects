import pygame
import sys
import asyncio
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

# Predefined some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (181, 218, 186)
VODKA = (191, 184, 244)
GRAY = (143, 134, 126)

# Screen information
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

DISPLAYSURF = pygame.display.set_mode((500, 500))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
game_running = True

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("circle.png")
        self.rect = self.image.get_rect()
        self.rect.center = (250, 250)
        self.speed = [5, 5]

    def move(self):
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        if self.rect.bottom > 487 or self.rect.top < 20:
            return False

        if self.rect.right > SCREEN_WIDTH or self.rect.left < 0:
            self.speed[0] *= -1

        return True

    def reverse_direction(self):
        self.speed[1] *= -1

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("rectangle.png")
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


async def show_game_over_screen():
    restart_button = pygame.Rect(200, 100, 100, 50)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                if restart_button.collidepoint(event.pos):
                    return True

        DISPLAYSURF.fill(VODKA)

        pygame.draw.rect(DISPLAYSURF, BLACK, restart_button)
        
        # Render the text for the restart button
        font = pygame.font.Font(None, 24)
        button_text = font.render("Restart", True, WHITE)
        text_rect = button_text.get_rect(center=restart_button.center)

        DISPLAYSURF.blit(button_text, text_rect.topleft)  # Blit the text onto the button surface
        pygame.display.update()
        FramePerSec.tick(FPS)
        await asyncio.sleep(0)  # Allow other tasks to run


async def play_game():
    global game_running  # Declare game_running as a global variable
    P1 = Player(250, 20)
    P2 = Player(250, 480)
    b = Ball()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        if game_running:
            P1.update()
            P2.update()
            if not b.move():
                game_running = False

            # Collision detection
            if b.rect.colliderect(P1.rect) or b.rect.colliderect(P2.rect):
                b.reverse_direction()

            DISPLAYSURF.fill(GRAY)
            P1.draw(DISPLAYSURF)
            P2.draw(DISPLAYSURF)
            b.draw(DISPLAYSURF)

            pygame.display.update()
            FramePerSec.tick(FPS)
        else:
            if await show_game_over_screen():
                game_running = True
                b.rect.center = (250, 250)


async def main():
    while True:
        await play_game()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()
